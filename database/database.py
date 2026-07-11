"""
MeshAnalyzer Pro
Database Engine
"""

import json
import sqlite3
from datetime import datetime
from pathlib import Path

from core.mesh import Mesh


class Database:

    def __init__(self):
        self.db_folder = Path("database")
        self.db_folder.mkdir(exist_ok=True)

        self.db_path = self.db_folder / "history.db"

        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS mesh_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT,
                name TEXT,
                filename TEXT,
                rows INTEGER,
                cols INTEGER,
                minimum REAL,
                maximum REAL,
                average REAL,
                total_range REAL,
                rms REAL,
                std REAL,
                mesh_json TEXT,
                favorite INTEGER DEFAULT 0,
                label TEXT DEFAULT '',
                note TEXT DEFAULT ''
            )
        """)

        self.ensure_history_columns()

        self.connection.commit()

    def ensure_history_columns(self):
        self.cursor.execute("PRAGMA table_info(mesh_history)")
        columns = {
            row[1]
            for row in self.cursor.fetchall()
        }

        migrations = {
            "favorite": "ALTER TABLE mesh_history ADD COLUMN favorite INTEGER DEFAULT 0",
            "label": "ALTER TABLE mesh_history ADD COLUMN label TEXT DEFAULT ''",
            "note": "ALTER TABLE mesh_history ADD COLUMN note TEXT DEFAULT ''",
        }

        for column, statement in migrations.items():
            if column not in columns:
                self.cursor.execute(statement)

        self.connection.commit()

    def save_mesh(self, mesh):
        self.cursor.execute("""
            INSERT INTO mesh_history (
                created_at,
                name,
                filename,
                rows,
                cols,
                minimum,
                maximum,
                average,
                total_range,
                rms,
                std,
                mesh_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            mesh.name,
            mesh.filename,
            mesh.rows,
            mesh.cols,
            mesh.minimum,
            mesh.maximum,
            mesh.average,
            mesh.total_range,
            mesh.rms,
            mesh.std,
            json.dumps(mesh.values)
        ))

        self.connection.commit()
        mesh.history_id = self.cursor.lastrowid
        return self.cursor.lastrowid

    def get_history(self):
        self.cursor.execute("""
            SELECT
                id,
                created_at,
                name,
                rows,
                cols,
                minimum,
                maximum,
                total_range,
                rms,
                favorite,
                label,
                note
            FROM mesh_history
            ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    def load_mesh_by_id(self, mesh_id):
        self.cursor.execute("""
            SELECT
                name,
                filename,
                mesh_json
            FROM mesh_history
            WHERE id = ?
        """, (mesh_id,))

        row = self.cursor.fetchone()

        if row is None:
            return None

        name, filename, mesh_json = row

        mesh = Mesh(
            name=name,
            filename=filename,
            values=json.loads(mesh_json)
        )
        mesh.history_id = mesh_id
        return mesh

    def load_previous_mesh(self, mesh):
        mesh_id = getattr(mesh, "history_id", None)

        if mesh_id is not None:
            self.cursor.execute("""
                SELECT id
                FROM mesh_history
                WHERE id < ?
                ORDER BY id DESC
                LIMIT 1
            """, (mesh_id,))
        else:
            self.cursor.execute("""
                SELECT id
                FROM mesh_history
                ORDER BY id DESC
                LIMIT 1 OFFSET 1
            """)

        row = self.cursor.fetchone()

        if row is None:
            return None

        return self.load_mesh_by_id(row[0])

    def update_history_metadata(self, mesh_id, label=None, note=None, favorite=None):
        fields = []
        values = []

        if label is not None:
            fields.append("label = ?")
            values.append(label)

        if note is not None:
            fields.append("note = ?")
            values.append(note)

        if favorite is not None:
            fields.append("favorite = ?")
            values.append(1 if favorite else 0)

        if not fields:
            return

        values.append(mesh_id)

        self.cursor.execute(
            f"UPDATE mesh_history SET {', '.join(fields)} WHERE id = ?",
            values
        )

        self.connection.commit()

    def get_history_item_metadata(self, mesh_id):
        self.cursor.execute("""
            SELECT favorite, label, note
            FROM mesh_history
            WHERE id = ?
        """, (mesh_id,))

        row = self.cursor.fetchone()

        if row is None:
            return {
                "favorite": False,
                "label": "",
                "note": "",
            }

        favorite, label, note = row

        return {
            "favorite": bool(favorite),
            "label": label or "",
            "note": note or "",
        }

    def clear_history(self):
        self.cursor.execute("""
            DELETE FROM mesh_history
        """)
        self.cursor.execute("""
            DELETE FROM sqlite_sequence
            WHERE name = 'mesh_history'
        """)

        self.connection.commit()

    def delete_history_item(self, mesh_id):
        self.cursor.execute("""
            DELETE FROM mesh_history
            WHERE id = ?
        """, (mesh_id,))

        self.resequence_history_ids()
        self.connection.commit()

    def resequence_history_ids(self):
        self.cursor.execute("""
            CREATE TEMPORARY TABLE mesh_history_resequence AS
            SELECT
                created_at,
                name,
                filename,
                rows,
                cols,
                minimum,
                maximum,
                average,
                total_range,
                rms,
                std,
                mesh_json,
                favorite,
                label,
                note
            FROM mesh_history
            ORDER BY id
        """)

        self.cursor.execute("""
            DELETE FROM mesh_history
        """)

        self.cursor.execute("""
            DELETE FROM sqlite_sequence
            WHERE name = 'mesh_history'
        """)

        self.cursor.execute("""
            INSERT INTO mesh_history (
                created_at,
                name,
                filename,
                rows,
                cols,
                minimum,
                maximum,
                average,
                total_range,
                rms,
                std,
                mesh_json,
                favorite,
                label,
                note
            )
            SELECT
                created_at,
                name,
                filename,
                rows,
                cols,
                minimum,
                maximum,
                average,
                total_range,
                rms,
                std,
                mesh_json,
                favorite,
                label,
                note
            FROM mesh_history_resequence
        """)

        self.cursor.execute("""
            DROP TABLE mesh_history_resequence
        """)

    def close(self):
        self.connection.close()

"""
MeshAnalyzer Pro
Project Serializer
.meshproj veri hazırlama
"""

from datetime import datetime
from core.config import Config


class ProjectSerializer:

    def __init__(self):
        self.config = Config()

    def mesh_to_dict(self, mesh):
        return {
            "name": mesh.name,
            "filename": mesh.filename,
            "rows": mesh.rows,
            "cols": mesh.cols,
            "values": mesh.values,
            "minimum": mesh.minimum,
            "maximum": mesh.maximum,
            "average": mesh.average,
            "total_range": mesh.total_range,
            "rms": mesh.rms,
            "std": mesh.std,
        }

    def create_project_data(self, mesh):
        return {
            "project_version": "1.0",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "mesh": self.mesh_to_dict(mesh),
            "settings": self.config.load(),
        }
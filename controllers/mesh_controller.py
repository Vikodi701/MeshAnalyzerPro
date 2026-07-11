"""
Mesh Analyzer Pro
Mesh Controller
"""

from PySide6.QtCore import QObject, Signal


class MeshController(QObject):

    meshLoaded = Signal(object)

    def __init__(self):
        super().__init__()

        self.mesh = None

    def set_mesh(self, mesh):

        self.mesh = mesh

        self.meshLoaded.emit(mesh)
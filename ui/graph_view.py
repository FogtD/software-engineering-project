import typing
from PyQt5 import QtGui
from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt
from graph_items.node_item import NodeItem

class GraphView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        # Stores the mouse mode for knowing if you'll place a node or edge
        self.mode = "none"
        # Stores the starting node for connecting an edge
        self.edge_start_node = None
        
    def set_mode(self, mode):
        self.mode = mode
        self.edge_start_node = None
     
    def mousePressEvent(self, event):
        # Get the user's mouse position within the scene
        scene_pos = self.mapToScene(event.pos())

        if event.button() == Qt.LeftButton:
            if self.mode == "node_place":
                new_node = NodeItem(scene_pos)
                self.scene().addItem(new_node)
                
            elif self.mode == "edge_start":
                item = self.scene().itemAt(scene_pos, self.transform())
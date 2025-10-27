import typing
from PyQt5 import QtGui
from PyQt5.QtWidgets import QGraphicsView, QInputDialog, QGraphicsSimpleTextItem
from PyQt5.QtCore import Qt
from graph_items.node_item import NodeItem
from graph_items.edge_item import EdgeItem

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
                default_name = self.scene().get_next_node_name()
                new_node = NodeItem(scene_pos, default_name) 
                self.scene().addItem(new_node)
                
            elif self.mode == "edge_start":
                item = self.scene().itemAt(scene_pos, self.transform())

                if isinstance(item, QGraphicsSimpleTextItem) and isinstance(item.parentItem(), NodeItem):
                    item = item.parentItem()

                # Check to make sure they clicked on a node
                if isinstance(item, NodeItem):
                    if self.edge_start_node == None:
                        self.edge_start_node = item
                    else:
                        new_edge = EdgeItem(self.edge_start_node, item)
                        self.scene().addItem(new_edge)

                        symbol, success = QInputDialog.getText(self, "Edge Symbol", "Enter transition symbol:")
                        if success:
                            new_edge.set_symbol(symbol)

                        self.edge_start_node = None
                else:
                    # Reset mouse mode if they don't click on a node
                    self.set_mode("none")
        super().mousePressEvent(event)

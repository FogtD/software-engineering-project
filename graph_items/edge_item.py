from PyQt5.QtWidgets import QGraphicsLineItem, QMenu
from PyQt5.QtCore import QLineF, Qt
from PyQt5.QtGui import QPen
from graph_items.node_item import NodeItem

class EdgeItem(QGraphicsLineItem):
    def __init__(self, node1: NodeItem, node2: NodeItem):
        super().__init__()
        self.node1 = node1
        self.node2 = node2

        # Edges will be in black with thickness 2
        self.setPen(QPen(Qt.black, 2))

        # Edges will appear below nodes
        self.setZValue(0)

        self.node1.edges.append(self)
        self.node2.edges.append(self)
        
        # This function actually draws the line and will be called whenever an edge is created or a node is moved that already has an edge
        self.update_position()

    def update_position(self):
        line = QLineF(self.node1.pos(), self.node2.pos())
        self.setLine(line)

    def contextMenuEvent(self, event):
        menu = QMenu()
        delete_action = menu.addAction("Delete Transition")
        action = menu.exec_(event.screenPos())

        if action == delete_action:
            self.scene().removeItem(self)
            if self in self.node1.edges:
                self.node1.edges.remove(self)
            if self in self.node2.edges:
                self.node2.edges.remove(self)

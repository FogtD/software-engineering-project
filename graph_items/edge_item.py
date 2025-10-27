from PyQt5.QtWidgets import QGraphicsLineItem, QMenu,  QGraphicsSimpleTextItem, QGraphicsItem
from PyQt5.QtCore import QLineF, Qt, QPointF
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

        self.symbol = ""
        self.text_item = QGraphicsSimpleTextItem(self.symbol)
        self.text_item.setZValue(1)

        self.node1.edges.append(self)
        if self.node1 != self.node2:
            self.node2.edges.append(self)
        
        # This function actually draws the line and will be called whenever an edge is created or a node is moved that already has an edge
        self.update_position()

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemSceneChange and value:
            value.addItem(self.text_item)
        return super().itemChange(change, value)

    def set_symbol(self, symbol):
        self.symbol = symbol
        self.text_item.setText(self.symbol)
        self.update_position()

    def update_position(self):
        line = QLineF(self.node1.pos(), self.node2.pos())
        self.setLine(line)

        mid_point = (self.node1.pos() + self.node2.pos()) / 2

        text_rect = self.text_item.boundingRect()
        offset_pos = mid_point - QPointF(text_rect.width() / 2, text_rect.height() / 2)

        self.text_item.setPos(offset_pos)

    def contextMenuEvent(self, event):
        menu = QMenu()
        delete_action = menu.addAction("Delete Transition")
        action = menu.exec_(event.screenPos())

        if action == delete_action:
            if self.scene():
                self.scene().removeItem(self.text_item)

            self.scene().removeItem(self)
            
            if self in self.node1.edges:
                self.node1.edges.remove(self)
            if self.node1 != self.node2:
                if self in self.node2.edges:
                    self.node2.edges.remove(self)

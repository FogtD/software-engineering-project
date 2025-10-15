from ossaudiodev import control_labels
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QGraphicsScene)
from PyQt5.QtCore import QSize
from ui.graph_view import GraphView

class PlaceholderMachineScene(QGraphicsScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setSceneRect(0,0,1920,1080)

class MachineEditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("State Flow Automata Visualizer")
        self.setGeometry(100, 100, 1200, 800)

        self.scene = PlaceholderMachineScene()
        self.view = GraphView(self.scene)
        
        self.node_button = QPushButton("Place Node")
        self.edge_button = QPushButton("Place Edge")
           
        # Sets the user's mouse mode to the correct type for placing edges/nodes
        self.node_button.clicked.connect(lambda: self.view.set_mode("node_place"))
        self.edge_button.clicked.connect(lambda: self.view.set_mode("edge_start"))
        
        # Defining the layout for the node and edge buttons
        control_layout = QHBoxLayout()
        control_layout.addWidget(self.node_button)
        control_layout.addWidget(self.edge_button)
        control_layout.addStretch(1)

        main_layout = QVBoxLayout()
        main_layout.addLayout(control_layout)
        main_layout.addLayout(self.view)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
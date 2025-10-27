from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QGraphicsScene)
from PyQt5.QtCore import QSize
from ui.graph_view import GraphView
from graph_items.node_item import NodeItem

class PlaceholderMachineScene(QGraphicsScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setSceneRect(0,0,1920,1080)

        self.node_counter = 0

    def get_next_node_name(self):
        name = f"q{self.node_counter}"
        self.node_counter += 1
        return name
       
    # Set a node to be an initial node and reset the previous initial node to a regular node
    def set_initial_node(self, new_initial_node):
        current_initial = None

        for item in self.items():
            if isinstance(item, NodeItem) and item.is_initial:
                current_initial = item
                break
        
            if current_initial and current_initial != new_initial_node:
                current_initial.is_initial = False
                current_initial.update()

            new_initial_node.is_initial = True
            new_initial_node.update()

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

        main_layout.addWidget(self.view)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
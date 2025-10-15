import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MachineEditorWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MachineEditorWindow()
    window.show()
    sys.exit(app.exec_())
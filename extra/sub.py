# DEBUG FILE
# old code of main.py pasted in this temporary file,
# Whilst learning the PyQt5 Library

'''
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (
    QApplication, 
    QLabel, 
    QMainWindow, 
    QWidget, 
    QVBoxLayout, 
    QHBoxLayout, 
    QTableWidget, 
    QListWidget,
    QPushButton,
    QTextEdit
)
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Stuff")
        self.setStyleSheet("background-color: white;")
        #self.setGeometry(0, 0, 900, 600)
        self.resize(900,600)

        main_layout = QVBoxLayout(self)

        #top bar
        top_bar = QHBoxLayout()
        title_label = QLabel("Metadata Sanitizer for File Sharing")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        top_bar.addWidget(title_label)
        top_bar.addStretch()
    
        help_button = QPushButton("Help/About")
        logs_button = QPushButton("View Logs")
        top_bar.addWidget(help_button)
        top_bar.addWidget(logs_button)
    
        main_layout.addLayout(top_bar)
    
        # === MAIN CONTENT (LEFT + RIGHT) ===
        content_layout = QHBoxLayout()
    
        # Left panel
        left_panel = QVBoxLayout()
        file_display = QTextEdit()
        file_display.setPlaceholderText("SELECTED FILE DISPLAY AREA")
        file_display.setReadOnly(True)
        left_panel.addWidget(file_display)
    
        upload_button = QPushButton("Upload File")
        left_panel.addWidget(upload_button)
    
        content_layout.addLayout(left_panel)
    
        # Right panel
        right_panel = QVBoxLayout()
        right_title = QLabel("Metadata Preview Area")
        right_title.setStyleSheet("font-size: 18px; font-weight: bold;")
        right_panel.addWidget(right_title)
    
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Remove?", "Metadata Field", "Value"])
        right_panel.addWidget(self.table)
    
        content_layout.addLayout(right_panel)
    
        main_layout.addLayout(content_layout)
    
        # === BOTTOM BAR ===
        bottom_bar = QHBoxLayout()
        bottom_bar.addStretch()
        sanitize_button = QPushButton("Sanitize")
        sanitize_button.setFixedSize(150, 50)
        bottom_bar.addWidget(sanitize_button)
        bottom_bar.addStretch()
    
        main_layout.addLayout(bottom_bar)
    
        # Connect signals
        upload_button.clicked.connect(self.new_click)
        sanitize_button.clicked.connect(self.on_click)
        help_button.clicked.connect(self.show_help)
        logs_button.clicked.connect(self.show_logs)

    def new_click(self):
        print("works")
    
    def on_click(self):
        print("works")

    def show_help(self):
        print("works")
    
    def show_logs(self):
        print("works")
        
        
        #main widget
        main_widget = QtWidgets.QWidget(self)
        label = QLabel("Label 1", self)
        label2 = QLabel("Label 2", self)
        label3 = QLabel("Label 3", self)
        label4 = QLabel("Label 4", self)
        label.setStyleSheet("color:orange;" "font-weight:bold;" "font-size:20px;")
        label2.setStyleSheet("color:red;" "font-weight:bold;" "font-size:20px;")
        label3.setStyleSheet("color:green;" "font-weight:bold;" "font-size:20px;")
        label4.setStyleSheet("color:blue;" "font-weight: bold;" "font-size:20px;")

        #assigning variables for Box Layouts
        hori = QHBoxLayout(main_widget)
        veri = QVBoxLayout(main_widget)
        hori.setSpacing(100)
        
        #horizontal
        hori.addWidget(label)
        hori.addWidget(label2)
        
        #vertical
        veri.addWidget(label3)
        veri.addWidget(label4)
        hori.addLayout(veri)


def main():
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
'''
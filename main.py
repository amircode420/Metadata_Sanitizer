# MAIN FILE

import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget,
    #QMainWindow, 
    QLabel, 
    QPushButton,
    QVBoxLayout,
    QTableWidget,
    QHBoxLayout,
    #QStatusBar,
    QTableWidgetItem,
    QCheckBox,
    QMessageBox,
    QTextEdit,
    QHeaderView
    )
#from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt #Qt class is used for alignments
from core.pdf_remover import extract_pdf_meta, sanitize_pdf
from core.image_remover import extract_img_meta, sanitize_img
from core.doc_remover import extract_doc_meta, sanitize_doc
from core.detector import detect_file_type
from core.helper import HelperWindow
from logger import OperationLogger, LogViewer

# STYLE SHEET VARIABLES
dark_bg = "#2b2b2b"
dark_wg = "#3c3c3c"
text_col = "#ffffff"
col_accent = "#692a2a"


# THE WHOLE APPLICATION CLASS
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Metadata Sanitizer for File Sharing")
        self.setStyleSheet(f"background-color: #1F2937; color: {text_col};")
        self.resize(900,600)
        self.logger = OperationLogger()
        #self.initUI()

        # MAIN LAYOUT 
        main_layout = QVBoxLayout(self)

        #upper widget
        top_bar = QHBoxLayout()
        title = QLabel("Metadata Sanitizer for File Sharing")
        title.setStyleSheet(f'''QLabel{{
                        font-family: "Cascadia Code";
                        font-weight: bold;
                        font-size: 30px; 
                        color: #00FFFF;
                    }}
                    ''')
        top_bar.addWidget(title)
        top_bar.addStretch()

        #UPPER BUTTONS
        help_button = QPushButton("Help")
        help_button.setStyleSheet(f'''QPushButton{{
                                  font-size: 15px;
                                  font-weight: bold;
                                  font-style: italic;
                                  background-color: #38BDF8;
                                  }}
                                  QPushButton:Hover{{
                                  background-color:#1E3A8A;
                                  }}''')
        log_button = QPushButton("View Logs")
        log_button.setStyleSheet(f'''QPushButton{{
                                font-size: 15px;
                                font-weight: bold;
                                font-style: italic;
                                background-color: #38BDF8;
                                color: white;
                                }}
                                QPushButton:Hover{{
                                background-color: #1E3A8A;
                                }}''')

        # UPPER BUTTON FUNCTIONALITY (HELP)
        

        help_button.clicked.connect(self.help)
        log_button.clicked.connect(self.logs)

        top_bar.addWidget(help_button)
        top_bar.addWidget(log_button)

        main_layout.addLayout(top_bar)

        # MID LAYOUT
        mid_layout = QHBoxLayout()

        # MID LAYOUT | LEFT FILE BOX
        file_box = QVBoxLayout() #mid area Vertical Layout for the file box.
        self.file_display = QTextEdit()
        self.file_display.setReadOnly(True)
        self.file_display.setPlaceholderText("No file Selected")
        self.file_display.setFixedWidth(270)
        self.file_display.setFixedHeight(450)
        self.file_display.setStyleSheet(f"background-color: {dark_wg};" "font-size: 15px;" f"color:{text_col};" f"border: 2px solid grey")
        file_box.addWidget(self.file_display)

        mid_layout.addLayout(file_box)

        # MID LAYOUT | RIGHT TABLE
        right_table = QVBoxLayout()
        self.table = QTableWidget(0,3)
        self.table.setHorizontalHeaderLabels(["Field", "Value", "Remove?"])
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch) # DEFAULT TABLE CONTENT BEHAVIOUR (INTERACTIVE) CHANGED TO STRETCH TO FIT ALL THE VALUES PERFECTLY (STRETCH)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        self.table.setStyleSheet(f'''QTableWidget{{
            background-color: {dark_wg};
            }}
            QHeaderView::section{{
            background-color: {dark_wg};
            color: {text_col};
            }}
            QTableCornerButton::section{{
            background-color: {dark_wg};
            border: none;
            }}
            QFont{{
            font: 15px;
            }}
            ''') # QTableCornerButton --> is the corner button that selects the entire table. Seperate component, Seperate Styling.
        right_table.addWidget(self.table)

        mid_layout.addLayout(right_table)
        mid_layout.setStretchFactor(self.table, 1)
        main_layout.addLayout(mid_layout)
        mid_layout.setContentsMargins(0,20,0,0)
    
        # down bar
        down_bar = QHBoxLayout()
        down_bar.addStretch()
        # Choose FIle button
        button = QPushButton("Choose File")
        button.setGeometry(10, 520, 160, 50)
        button.setFixedSize(QtCore.QSize(160, 50))
        button.setStyleSheet(f'''QPushButton{{
            background-color: #38BDF8; font-size: 20px; 
            color: {text_col}; border-radius: 10px; border:none; font-family: arial; font-weight: bold; 
            }}
            QPushButton:hover {{
            background-color: #FBBF24;
                             }}''')
        button.clicked.connect(self.new_click)
        down_bar.addWidget(button)
        down_bar.addStretch(1)

        #sanitize Button
        button2 = QPushButton("Sanitize", self)
        #button2.setGeometry(740, 520, 150,50)
        #button2.resize(740, 320)
        button2.setStyleSheet(f'''QPushButton{{
            font-size: 20px; 
            color:{text_col};
            background-color: #38BDF8;
            padding: 10px 20px; 
            border-radius: 10px;
            border:none;
            font-family: arial;
            font-weight: bold;
            border: None;
            }}
                              
            QPushButton:hover{{
            background-color: #34D399;
            }}
            ''')
        button2.setFixedSize(QtCore.QSize(150, 50))
        button2.clicked.connect(self.on_click) #button.clicked is the "signal" after which the button is clicked and allows it to perfom the function its supposed to.
        down_bar.addWidget(button2)
        down_bar.addStretch()
        main_layout.addLayout(down_bar)

    #functions for populating the Table with metadata values to choose.
    def populate_table(self, metadata: dict):
        self.table.setRowCount(0)
        self.table.setRowCount(len(metadata))

        font_set = self.table.font()
        font_set.setPointSize(9)
        self.table.setFont(font_set)

        for row, (key, value) in enumerate(metadata.items()):
            # column 0: Field Populator
            item_key = QTableWidgetItem(key)
            item_key.setFlags(item_key.flags() ^ Qt.ItemIsEditable)
            self.table.setItem(row, 0, item_key)

            #column 1: "Value" Populator
            item_value = QTableWidgetItem(value)
            item_value.setFlags(item_value.flags() ^ Qt.ItemIsEditable)
            self.table.setItem(row, 1, item_value)

            #column 2: "Remove? checkboxes"
            checkbox = QCheckBox()
            cell_widget = QWidget()
            layout = QHBoxLayout(cell_widget)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0,0,0,0)
            self.table.setCellWidget(row, 2, cell_widget)

    # GET THE FIELDS THAT ARE CHECKED IN UI FOR REMOVAL
    def get_field_rem(self):
        fields = []
        for row in range(self.table.rowCount()):
            cell_widget = self.table.cellWidget(row, 2)
            if cell_widget:
                checkbox = cell_widget.findChild(QCheckBox) # GETTING THE CHILD OF cell_widget THAT IS QCheckBox. --> "findChild"
                if checkbox and checkbox.isChecked():
                    field_item = self.table.item(row, 0) # GET FIELD NAME (EG : AUTHOR)
                    if field_item:
                        #print(" REMOVING : ", field_item.text())
                        fields.append(field_item.text())
        return fields
            
    
    # Functionality of Choose File Button
    def new_click(self):
        self.file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self , "Open Files", directory="", filter="ALL Files (*.*);; PDF Document (*.pdf);; Word (*.docx);; Image (*.jpg)")
        if self.file_name:
            self.file_display.setText(self.file_name)

            file_type = detect_file_type(self.file_name)

            try:
                # PDF METADATA DISPLAY
                if file_type == "pdf":
                    meta1 = extract_pdf_meta(self.file_name)
                    self.populate_table(meta1)
                # DOCX METADATA DISPLAY
                elif file_type == "docx":
                    meta2 = extract_doc_meta(self.file_name)
                    self.populate_table(meta2)
                # IMAGE METADATA DISPLAY
                elif file_type == "image":
                    meta3 = extract_img_meta(self.file_name)
                    self.populate_table(meta3)
                else:
                    QMessageBox.critical(self, "Error", f"Invalid File Format {self.file_name}")
            except Exception as e:
                self.table.setRowCount(0)
                QMessageBox.critical(self, "Error", "Failed to Read Metadata")
                self.logger.log_operation(
                    FileName = self.file_name,
                    FilePath = self.file_name,
                    FileType = file_type,
                    Status = "Failed",
                    RemovedFields = str(e)
                )
                print(e)

        else:
            print("This works")
 
    # FUNCTIONALITY OF SANITIZE BUTTON
    def on_click(self): 
        if not hasattr(self, "file_name") or not self.file_name:
            QMessageBox.warning(self, "No File Error", "Please choose a valid File First.")
            return

        base, ext = os.path.splitext(self.file_name) # BASE = base File name, EXT = file extenstion.
        out_path = base + "_sanitized" + ext # saving file with "_sanitized" tail to show that its sanitized
        
        file_type = detect_file_type(self.file_name)
        fields_rem = self.get_field_rem()
        try:
            # PDF SANITIZATION
            if file_type == "pdf":
                sanitize_pdf(self.file_name, out_path, fields_rem)
                print("REMOVING PDF METADATA: ", fields_rem)
                #print(file_type)
                QMessageBox.information(
                    self,
                    "Sanitized Successfully",
                    f"File has been Sanitized and saved as : {out_path}"
                )
            # DOCX SANITIZATION 
            elif file_type == "docx":
                sanitize_doc(self.file_name, out_path, fields_rem)
                print("REMOVING DOCX METADATA: ", fields_rem)
                #print(file_type)
                QMessageBox.information(
                    self,
                    "Sanitized Successfully",
                    f"File has been Sanitized and saved as : {out_path}"
                )
            # IMAGE SANITIZATION
            elif file_type == "image":
                sanitize_img(self.file_name, out_path, fields_rem)
                print("REMOVING IMG METADATA: ", fields_rem)
                #print(file_type)
                QMessageBox.information(
                    self,
                    "Sanitized Successfully",
                    f"File has been Sanitized and saved as : {out_path}"
                )
            #self.table.setRowCount(0)
            # LOGGING OPERATION
            self.logger.log_operation(
                FileName = self.file_name,
                FilePath = self.file_name,
                FileType = file_type,
                Status = "Success",
                RemovedFields = str(fields_rem)
            )
                #print(self.logger.view_log()) # TEMPORARY VIEWING FOR LOGS
        except Exception as e:
            QMessageBox.critical(self, "Error", "Failed to Sanitize")
            self.logger.log_operation(
                    FileName = self.file_name,
                    FilePath = self.file_name,
                    FileType = file_type,
                    Status = "Fail",
                    RemovedFields = str(fields_rem)
                )
            print(e)
        
        # CLEARS THE TABLE
        self.table.setRowCount(0)
        self.file_display.clear()

        print("You sanitized the file")

    #Help Button FUNCTIONALITY
    def help(self):
        help_win = HelperWindow(self)
        help_win.exec_()
        print("Help works")

    # VIEWING LOGS FUNCTIONALITY
    def logs(self):
        self.log_viewer = LogViewer(self.logger)
        self.log_viewer.exec_()

        print("PRINTING LOGS:\n ", self.logger.view_log())
        print("Log Works")


# FUNCTION TO KEEP WINDOW RUNNING 
def main():
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) #execute method "exec_()" gives the application the ability to stay open and not close immediately which is a PyQt5 default.

if __name__ == "__main__":
    main()
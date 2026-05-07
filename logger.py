import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QPushButton

# LOGGING OPERATION 
class OperationLogger:
    def __init__(self, db_path = "operations.db"):
        self.db_path = db_path # STORE IN VARIABLE SO IT IS USABLE IN EVERY FUNCTION
        self.init_db()

    def init_db(self):
        # INITIALIZE DATABASE
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # CREATE TABLE IF DOES NOT EXIST

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS OperationLog(
                       OperationID INTEGER PRIMARY KEY AUTOINCREMENT,
                       Timestamp TEXT,
                       FileName TEXT,
                       FilePath TEXT,
                       FileType TEXT,
                       Status TEXT,
                       RemovedFields TEXT
                        )
                       ''')
        
        conn.commit() # COMMIT QUERY AND SAVE TABLE
        conn.close() # CLOSE CONNECTION

    def log_operation(self, FileName, FilePath, FileType, Status, RemovedFields):
        # LOGGING FUNCTION
    
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        Timestamp = str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")) # strftime() is used to format the datetime object into a string
        print(Timestamp)
        cursor.execute('''INSERT INTO OperationLog(
                        Timestamp, FileName, FilePath, FileType, Status, RemovedFields)
                    VALUES(?,?,?,?,?,?)
                    ''', (Timestamp, FileName, FilePath, FileType, Status, RemovedFields)) # USING (?) is a security measure to prevent SQL Injection
        
        conn.commit()
        conn.close()
        
    def view_log(self):
        # VIEW LOG IN TERMINAL (TEMP)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM OperationLog ORDER BY Timestamp DESC")
        return cursor.fetchall()

# VIEWING LOGS
class LogViewer(QDialog): # QDIALOG MAKES IT INTO A POP-UP WINDOW
    def __init__(self, logger, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Operation Logs")
        self.resize(800, 600)
        self.setStyleSheet(f"font-size: 15px; background-color: #2b2b2b; color: #ffffff;")

        layout = QVBoxLayout()

        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)

        back_btn = QPushButton("Back to Sanitizer")
        back_btn.clicked.connect(self.close) # Closes window on click

        layout.addWidget(self.log_display)
        layout.addWidget(back_btn)
        self.setLayout(layout)

        self.load_logs(logger)

    def load_logs(self, logger):
        logs = logger.view_log()
        log_text = "OPERATIONID | TIMESTAMPS | FILENAME | FILETYPE | FILEPATH | STATUS | REMOVEDFIELDS\n"
        log_text += "-" * 145 + "\n"

        for log in logs:
            OperationID, TimeStamp, FileName, FileType, FilePath, Status, RemovedFields = log
            log_text += f" {OperationID} | {TimeStamp} | {FileName} | {FileType} | {FilePath} | {Status} | {RemovedFields}\n\n"

        self.log_display.setText(log_text)


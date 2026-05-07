# HELP BUTTON WINDOW

from PyQt5.QtWidgets import(
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QWidget
    )
from PyQt5.QtCore import Qt

# STYLE SHEET VARIABLES from main.py
dark_bg = "#2b2b2b"
dark_wg = "#3c3c3c"
text_col = "#ffffff"
col_accent = "#692a2a"

class HelperWindow(QDialog): # QDIALOG MAKES IT A POP WINDOW
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("User Manual - Metadatata Sanitizer for File Sharing")
        self.setFixedSize(800, 700)
        self.setStyleSheet(f"background-color: {dark_bg}; color: {text_col};")
        #self.setWindowFlag(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        layout = QVBoxLayout(self)
        
        # SCROLL AREA
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet(f"background-color: {dark_wg}; border: none;")

        content = QWidget()
        content_layout = QVBoxLayout(content)

        #guide_content
        guide_content = """
        <!-- USING HTML WITH CSS PROPERTIES -->
        <center><h2 style='color: #00FFFF;'><b> Metadata Sanitizer for File Sharing | User Manual </b></h2></center>
        
        <h3 style='color: #32CD32;'> What is Metadata?</h3>
        <p>Metadata is basically data about data. It shows how a piece data came to be, where it came from and what was used to create it.
        it includes important information like:</p>
        <ul>
            <li><b>Author name</b> - Who created the file</li>
            <li><b>Creation date</b> - When the file was made</li>
            <li><b>Software used</b> - What program created it</li>
            <li><b>Camera details</b> - For photos (GPS, camera model, settings)</li>
            <li><b>Document properties</b> - Title, subject, keywords</li>
            <li><b>Comments</b> - Notes or revisions history</li>
        </ul>
        
        <h3 style='color: #32CD32;'> Why Remove Metadata?</h3>
        <p>When sharing files publicly, metadata can reveal sensitive information such as:</p>
        <ul>
            <li> Your location (from GPS data in photos)</li>
            <li> Your identity (author names, usernames)</li>
            <li> Your software and system details</li>
            <li> Document revision history</li>
        </ul>
        <p> These pieces of information are more sensitive than you think. <br> Hence sanitizing your File should be a priority before you share it online </br></p>
        <h3 style='color: #32CD32;'><u> Simple Guide | How to Use This Tool</u></h3>
        
        <h4>Step 1: Choose a File</h4>
        <p>Click the <b>"Choose File"</b> button to select a file to sanitize.</p>
        <p><b>Supported formats for this tool:</b> PDF, Word documents (.docx), Images (.jpg, .jpeg)</p>
        
        <h4>Step 2: Review Metadata</h4>
        <p>After selecting a file, you'll see all metadata fields in the table:</p>
        <ul>
            <li><b>Field</b> - The metadata Field name</li>
            <li><b>Value</b> - The current metadata value</li>
            <li><b>Remove?</b> - Check boxes to select what you want to remove</li>
        </ul>
        
        <h4>Step 3: Select Metadata to Remove</h4>
        <p>Check the boxes next to metadata fields you want to remove:</p>
        <ul>
            <li> Check = Remove this metadata</li>
            <li> Uncheck = Keep this metadata (THIS IS THE DEFAULT STATE OF THE CHECKBOXES)</li>
        </ul>
        
        <h4>Step 4: Sanitize the File</h4>
        <p>Click the <b>"Sanitize"</b> button to create the Sanitized File</p>
        <ul>
            <li> Original file doesn't change</li>
            <li> A New file saved with "<file_name>_sanitized"</li>
            <li> Success message shows the new file location</li>
        </ul>

        <h5><b> NOTE: SOME FILES MAY NOT HAVE METADATA DUE TO ALREADY BEING REMOVED PREVIOUSLY 
        HENCE LEADING TO A BLANK TABLE WHEN A FILE IS CHOSEN</b></h5>
        
        <h3 style='color: #32CD32;'><u> -- Supported File Types -- </u></h3>
        
        <h4 style='color: #A5D6A7;'> PDF Files</h4>
        <p> It Removes: Author, title, subject, keywords, creator, producer, creation date, modification date</p>
        <h6><i> It changes the "Producer" tag to "NULL_VALUE" as the used software would be displayed otherwise </i></h6>
        
        <h4 style='color: #A5D6A7;'> Word Documents (.docx)</h4>
        <p>It Removes: Author, title, subject, keywords, comments, revision history, custom properties</p>
        
        <h4 style='color: #A5D6A7;'> Images (.jpg, .jpeg)</h4>
        <p>It Removes: Camera make/model, GPS coordinates (ExifTag), date taken, software info, comments</p>
        
        <h3> Things to Remember before you use the Application </h3>
        <ul>
            <li><b>Backup originals</b> - Keep original files before sanitizing</li>
            <li><b>Review carefully</b> - Check what metadata exists before removing</li>
            <li><b>Organize files</b> - Save sanitized files in a separate folder</li>
            <li><b>Double-check</b> - Verify the sanitized file by checking it again in the tool</li>
        </ul>
        
        <h3 style='color: #32CD32;'><u> FAQs </u></h3>
        
        <h4>Q: Does this tool affect file quality or corrupt the file?</h4>
        <p>A: No! Only metadata is removed. The actual content (text, images, formatting) remains exactly the same and the file is intact</p>
        
        <h4>Q: Can any metadata be recovered after removal?</h4>
        <p>A: No, once metadata is sanitized, it's permanently removed from the new file.</p>
        
        <h4>Q: Do You lose your main file? </h4>
        <p>A: NO! The tool creates a new sanitized file to preserve your original. You can delete it later if satisfied.</p>

        <h3 style='color: #32CD32;'><u> Privacy & Security </u></h3>
        <ul>
            <li><b>This tool works entirely on your computer</b></li>
            <li><b>No files are uploaded to external servers.</b></li>
            <li><b>Your privacy is protected.</b></li>
        </ul>
       
        
        <div style='margin-top: 20px; padding: 10px; background-color: {dark_wg}; border-radius: 5px;'></div>

        <h6><b><br> This is a security Tool Made for securing the privacy of individuals. Future Works May implement advanced File Cleansing and Additional Features</br><b></h6>
        <center><h6><i><br> THIS TOOL WAS CREATED BY Amir Fardeen </br></i></h6></center> 
        """

        help_label = QLabel(guide_content)
        help_label.setTextFormat(Qt.RichText)
        help_label.setWordWrap(True) # Long text can wrap to next line
        help_label.setStyleSheet(f"""
            QLabel{{
                color : {text_col};
                font-size: 15px;
                padding: 15px;
                background-color: {dark_wg};
                border-radius: 5px;
            }}
            h4{{
                font-size: 20px;
            }}
                                 """)
        
        # ADDING ALL WIDGETS TO LAYOUTS
        content_layout.addWidget(help_label)
        scroll.setWidget(content)
        layout.addWidget(scroll)

        # CLOSE BUTTON
        close_btn = QPushButton("Close")
        close_btn.setStyleSheet(f"background-color: {col_accent}")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)
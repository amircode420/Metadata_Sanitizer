# simple FILE DETECTION. python-magic
import magic

def detect_file_type(file_path):
    try:
        mime_detect = magic.Magic(mime = True)
        file = mime_detect.from_file(file_path)
        print(f"Detected File: {file}") #--> to get detected MIME header 

        if "application/pdf" in file:
            return "pdf"
        elif "application/vnd.openxmlformats-officedocument.wordprocessingml.document" in file or "application/octet-stream" in file or "application/zip" in file:
            return "docx"
        elif "image/jpeg" in file:
            return "image"
        else:
            return "Unknown"
    
    except ValueError as e:

        print(e)
        return "unknown"

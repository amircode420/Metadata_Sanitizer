#PDF Metadata Extractor
from PyQt5.QtWidgets import QMessageBox
from pypdf import PdfReader, PdfWriter
import os

# EXTRACTION FUNCTION
def extract_pdf_meta(pdf_path: str):
    reader = PdfReader(pdf_path) #parsing the file

    if reader.is_encrypted:
        QMessageBox.warning(None, "Warning", "Password Protected")
    
    meta = reader.metadata or {} #reading the file metadata
    clean_meta = {}
    for key, value in meta.items():
        if isinstance(key, str) and key.startswith('/'): #Checking whether key is str and has "/"
            clean_key = key[1:] ##slicing the "/" from the keys to make it neat
        else:
            clean_key = str(key)
        
        clean_meta[clean_key] = str(value) #turn value in string
        #print(clean_meta)
    return clean_meta

# SANITIZATION FUNCTION
def sanitize_pdf(in_path: str, out_path: str, fields_rem: list = None):
    reader = PdfReader(in_path)
    writer = PdfWriter()
    #writer.add_metadata({})

    # GET ALL PAGES
    for page in reader.pages:
        writer.add_page(page)

    # Choosing Metadata To Remove
    main_meta = reader.metadata or {}

    info = {} # DICT TO HOLD PDF METADATA
    for k, v in main_meta.items():
        clean_key = str(k)
        if clean_key.startswith("/"):
            clean_key = clean_key[1:]
        info[clean_key] = str(v)
    
    # IF FIELDS_REM is EMPTY, ALL THE METADATA WILL BE REMOVED
    if not fields_rem:
        print("REMOVING ALL METADATA")
        writer.add_metadata({})
        writer.add_metadata({"/Producer": "NULL VALUE"}) # CUSTOM PRODUCER TO OVERWRITE DEFAULT "PYPDF" VALUE

    # REMOVE ONLY WHATS CHOSEN
    else:
        normal_key = []
        for k in fields_rem:
            clean_key = k
            if clean_key.startswith("/"): # CHECKS IF KEY HAS "/"
                clean_key = clean_key[1:] # REMOVES THE "/" if FOUND
            normal_key.append(clean_key) # APPENDS THE CLEAN KEY WITHOUT "/""

        # DICTIONARY TO HOLD WANTED KEYS
        new_meta = {}
        for k, v in info.items():
            if k in normal_key: 
                #all_rem.append(k)
                print("REMOVING: ", k) # PRINT STATEMENT TO SEE WHAT'S BEING REMOVED IN THE TERMINAL
                continue
            else:
                # ADDING BACK THE SLASH BECAUSE pypdf's WRITER EXPECTS THE LEADING SLASH
                new_meta["/" + k] = v
            print("WRITING BACK METADATA: ", new_meta)
        '''
        if new_meta:
            new_meta["/Producer"] = "NULL_VALUE" # CUSTOM PRODUCER TO OVERWRITE DEFAULT PYPDF VALUE
        '''
        writer.add_metadata(new_meta)
        writer.add_metadata({"/Producer":"NULL_VALUE"}) # THIS STATEMENT OVERWRITES THE DEFAULT pypdf PRODUCER VALUE

    # SAVE THE NEW_FILE BACK INTO THE FOLDER
    with open(out_path, "wb") as f: # "wb" ensures that PDF FILES dont GET CORRUPTED
        writer.write(f) # WRITES ALL THE CONTENTS BACK INTO A PDF_FILE
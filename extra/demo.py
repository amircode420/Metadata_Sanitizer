# THIS FILE IS PURELY A DEBUG FILE, WITH ALL THE EXTRACTED CODE FROM DIFFERENT FILES JUST TO MANAGE THE CODE IN THE MAIN FILE. 
# I WILL USE THE SNIPPET I PASTE HERE IF NEEDED LATER

'''
THESE BLOCKS ARE FROM image_remover.py 

# TRYING TO EXTRACT METADATA WITH PILLOW 

try:
    image = Image.open(img_path)
    exif_pil = image._getexif()
    if exif_pil:
        for tag, value in exif_pil.items():
            decode_tag = TAGS.get(tag, tag)
            meta[decode_tag] = str(value)

except Exception as e:
    print(e)
'''

'''
# TRYING TO EXTRACT METADATA WITH PIEXIF

    try:
        image = piexif.load(img_path)
        print(image["GPS"])
        if image:
            for ifd in image:
                for tag, value in image[ifd].items():
                    decoded = TAGS.get(tag, tag)
                    meta[decoded] = str(value)
    
    except Exception as e:
        print(e)
    
# THIS PARTICULAR BLOCK OF CODE IS ANOTHER VERSION OF PIEXIF EXTRACTION LOGIC, WHERE the ifd is not looped through.... i.e (for ifd in image) 
        
    try:
        image = piexif.load(img_path)
        if image:
            for tag, value in image.items():
                decoded = TAGS.get(tag, tag)
                meta[decoded] = str(value)
                print(meta.items())
    
    except Exception as e:
        print(e)

    
'''


'''
# THIS IS THE "sanitize_img()" function block. I have pasted it here so that my img_remover.py is clean and IF i need this, ill copy this back as this code works and have fewer bugs.
    try:
        img = piexif.load(img_path)
        if not fields_rem:
            # REMOVE ALL METADATA
            piexif.remove(img_path, out_path)
            print("REMOVED ALL IMAGE METADATA")
        else:
            # REMOVING ONLY WHATS CHOSEN
            exif_dict = img # LOADING ALL THE IMAGE METADATA
            for tag, value in exif_dict.items():
                decoded = TAGS.get(tag, tag)
                if decoded in fields_rem:
                    try:
                        piexif.remove(value)
                    except Exception as e:
                        print(e)

                # THIS BLOCK IS A SMALL CHUNK OF THE SANITIZE_IMG() function. It turns the tags into human readable form.        
                for tag in list(exif_dict[ifd].keys()):
                    tag_info = piexif.TAGS[ifd].get(tag)
                    name = tag_info["name"] if tag_info else tag
                    if name in fields_rem:
                        del exif_dict[ifd][tag]
            piexif.insert(piexif.dump(exif_dict), img_path)




                    
        piexif.insert(exif_dict, out_path)
'''
    

### -------------------------------------------------------------------------------------------------------------------------- ###

'''
These are the blocks from main.py 

# PDF METADATA DISPLAY
try:
    meta = extract_pdf_meta(self.file_name)
    print("DISPLAYING META ITEM: ", list(meta.items()))
    self.populate_table(meta)
    #print("Dict: ", meta)
    #print(len(meta))

#Handling Exceptions
except Exception as e:
    QMessageBox.critical(self, "Error", "Failed to read Metadata")
'''            
'''
# DOCX METADATA DISPLAY
try:
    meta2 = extract_doc_meta(self.file_name)
    print("DISPLAYING META ITEMS: ", meta2.items())
    self.populate_table(meta2)
except ValueError as e:
    QMessageBox.critical(self, "Error", "Failed to read Metadata")
'''

'''
# IMG METADATA DISPLAY
try:
    meta3 = extract_img_meta(self.file_name)
    print("DISPLAYING META ITEMS: ", meta3.items())
    self.populate_table(meta3)
except Exception as e:
    QMessageBox.critical(self, "Error", "Failed to read Metadata")
'''
### -----------------------------------------------------------------------------------------------------###
'''
FOR METADATA SANITIZATION

# PDF SANITIZATION
try: 
    fields_rem = self.get_field_rem()
    print(" REMOVING : ", fields_rem)
    sanitize_pdf(self.file_name, out_path, fields_rem)

    QMessageBox.information(
        self,
        "Sanitized Successfully",
        f"File Has been Sanitize and Saved as: {out_path}"
    )
except Exception as e:
    QMessageBox.critical(self, "Error", "Faile to Sanitize. :(")
'''
''''
# DOCX SANITIZATION
try:
    fields_rem = self.get_field_rem()
    print("REMOVING DOCX METADATA: ", fields_rem)
    sanitize_doc(self.file_name, out_path, fields_rem)

    QMessageBox.information(
        self,
        "Sanitized Successfully",
        f"File has been Sanitized and saved as: {out_path}"
    )

except:
    QMessageBox.critical(self, "Error", "Failed to Sanitize")
'''

'''
# IMG SANITIZATION
try:
    fields_rem = self.get_field_rem()
    print("REMOVING IMAGE METADATA: ", fields_rem)
    sanitize_img(self.file_name, out_path, fields_rem)

    QMessageBox.information(
        self,
        "Sanitized Succesfully",
        f"File Has been Sanitized and saved as: {out_path}"
    )
except Exception as e:
    QMessageBox.critical(self, "Error", "Failed to Sanitize")
    print(e)
'''
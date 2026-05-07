# FOR IMAGE METADATA EXTRACTION
#from PIL import Image
#from PIL.ExifTags import TAGS
import piexif
import shutil

def extract_img_meta(img_path: str): 
# TRYING TO EXTRACT METADATA WITH PIEXIF
    meta = {}
    try:
        # LOAD METADATA --> piexif.load() loads it as a dictionary
        image = piexif.load(img_path)
        for ifd, data in image.items():
            if not isinstance(data, dict):
                continue
            for tag, value in data.items():
                tag_info = piexif.TAGS[ifd].get(tag)
                name = tag_info["name"] if tag_info else str(tag)
                meta[name] = str(value)
    except NameError as e:
        print(e)

    return meta

def sanitize_img(img_path: str, out_path: str, fields_rem: list=None): 
    try:
        img = piexif.load(img_path)
        if not fields_rem:
            # REMOVE ALL METADATA
            shutil.copy2(img_path, out_path) # COPYING THE FILE THEN REMOVING THE METADATA FROM THAT FILE
            piexif.remove(out_path)
            print("REMOVED ALL IMAGE METADATA")
        else:
            # REMOVING ONLY WHATS CHOSEN
            new_dict = {} # LOADING ALL THE IMAGE METADATA
            for ifd in img:
                if ifd == 'thumbnail':
                    new_dict[ifd] = img[ifd]
                    continue
                if not isinstance(img[ifd], dict): #SKIPPING NON-DICTIONARY ITEMS
                    new_dict[ifd] = img[ifd]
                    continue
                new_dict[ifd] = {}
                for tag, value in img[ifd].items():
                    tag_info = piexif.TAGS[ifd].get(tag)
                    name = tag_info["name"] if tag_info else str(tag)
                    # IF A TAG ISNT FOR REMOVAL, KEEP IT
                    if name not in fields_rem:
                        new_dict[ifd][tag] = value
                
            # CONVERTING EXIF DICTIONARY TO BINARY EXIF DATA.
            """   TO WORKAROUND the

            ["dump" got wrong type of exif value 41729 in Exif IFD. Got as <class 'int'>] input error 
            
            BY MANUALLY CHANGING THE VALUE OF 41729 to a byte i.e --> b'1'  """

            new_dict['Exif'][41729] = b'1'
            exif_bin = piexif.dump(new_dict)

            # NEW EXIF DATA PUT INTO NEW CLEANED FILE
            shutil.copy2(img_path, out_path)
            piexif.insert(exif_bin, out_path)
            print(f"REMOVED FIELDS: {fields_rem}")

    except Exception as e:
        print(e)
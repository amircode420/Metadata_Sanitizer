# DEBUG FILE
# This file holds the code from image_remover which was pasted whilst making corrections to the code,
# so that the old code pasted can be used later if needed.

# FOR IMAGE METADATA EXTRACTION
'''
from PIL import Image
from PIL.ExifTags import TAGS
import piexif

def extract_img_meta(img_path: str):
    
    meta = {}

# TRYING TO EXTRACT METADATA WITH PIEXIF
    
    try:
        image = piexif.load(img_path)
        if image:
            for tag, value in image.items():
                decoded = TAGS.get(tag, tag)
                meta[decoded] = str(value)
                print(meta.items())
    
    except Exception as e:
        print(e)

    return meta

def sanitize_img(img_path: str, out_path: str, fields_rem: list=None):
    try:
        img = piexif.load(img_path)
        if not fields_rem:
            # REMOVE ALL METADATA
            piexif.remove(img_path)
            print("REMOVED ALL IMAGE METADATA")
        else:
            # REMOVING ONLY WHATS CHOSEN
            exif_dict = img# LOADING ALL THE IMAGE METADATA
            for tag, value in exif_dict.items():
                decoded = TAGS.get(tag, tag)
                if decoded in fields_rem:
                    try:
                        piexif.remove(exif_dict, tag)
                    except Exception as e:
                        print(e)
                    
        piexif.insert(exif_dict, out_path)

    except Exception as e:
        print(e)
'''
# THIS FILE WAS USED TO CREATE TEST FILES TO TEST THE APPLICATION

import os
from pypdf import PdfWriter, PdfReader, PageObject
#from docx import Document
#from PIL import Image
#import piexif
'''
img = Image.new('RGB', (100,100), color='red')

#img.save("text.jpg", quality=100)

#piexif.remove("text.jpg")

# creating image metadata using piexif for dummy image.
exif_dict = {
    "0th": {
        piexif.ImageIFD.Make: "RANDOM",
        piexif.ImageIFD.Model: "RANDOMM_MODEL",
        piexif.ImageIFD.DateTime: "1900:01:01 22:30:00",
        piexif.ImageIFD.Software: "RANDOM SPECIAL SOFTWARE"
    },

    "Exif":{
        piexif.ExifIFD.DateTimeOriginal: "1900:01:01 22:30:00",
        piexif.ExifIFD.DateTimeOriginal: "1900:01:01 22:30:00",
        piexif.ExifIFD.ExposureTime: (0,0),
        piexif.ExifIFD.FNumber: (0,0),
        piexif.ExifIFD.FocalLength: (0,0)
    },

    "GPS": {
        piexif.GPSIFD.GPSLatitudeRef: b'N',  # North
        piexif.GPSIFD.GPSLatitude: ((34, 1), (17, 1), (51, 1)),  
        piexif.GPSIFD.GPSLongitudeRef: b'W',  # West
        piexif.GPSIFD.GPSLongitude: ((118, 1), (14, 1), (36, 1)),  
        piexif.GPSIFD.GPSAltitudeRef: 0,  
        piexif.GPSIFD.GPSAltitude: (100, 1), 
    }
}
 
# Convert to EXIF bytes
exif_bites = piexif.dump(exif_dict)
 
# Save image with GPS data only
img.save("text.jpg", exif=exif_bites, quality=100)
'''

'''
doc = Document()
doc.add_paragraph("THIS IS A TEST")
doc.save("new_test.docx")
'''


pdftest = PdfWriter()

custom_meta = {
    "/Author": "John DOE",
    "/Title": "TOTALLY NORMAL PDF FILE",
    "/Subject": "\x00VERY \x01NICE SUBJECT",
    "/Keywords": "Test, meta, aliens"
}

pdftest.add_metadata(custom_meta)

pg = PageObject.create_blank_page(width=600, height=700)
pdftest.add_page(pg)

#pdftest.add_metadata({})
with open("new_test.pdf", "wb") as f:
    pdftest.write(f)

# FOR DOCX METADATA EXTRACTION
from docx import Document 
from datetime import datetime

# FUNCTION TO EXTRACT DOCX METADATA

def extract_doc_meta(doc_path: str):
    doc = Document(doc_path)
    core = doc.core_properties # ACCESSING CORE DOCUMENT METADATA

    if not core:
        return {}

    meta = {}
    # DOCX METADATA EXISTS AS STRING BY DEFAULT
    meta["title"] = core.title if core.title else "empty"   # INLINE IF ELSE STATEMENT TO RETURN "EMPTY" IF FIELD EMPTY
    meta["author"] = core.author if core.author else "empty"
    meta["subject"] = core.subject if core.subject else "empty"
    meta["keywords"] = core.keywords if core.keywords else "empty"
    meta["content_status"] = core.content_status if core.content_status else "empty"
    meta["category"] = core.category if core.category else "empty"
    meta["comments"] = core.comments if core.comments else "empty"
    meta["created"] = str(core.created) if core.created else "empty"
    meta["modified"] = str(core.modified) if core.modified else "empty"
    meta["last_modified_by"] = str(core.last_modified_by) if core.last_modified_by else "empty"
    meta["revision"] = str(core.revision) if core.revision else "empty"

    return meta

# SANITIZATION FUNCTION
def sanitize_doc(doc_path: str, out_path: str, fields_rem: list = None):
    doc = Document(doc_path)
    core = doc.core_properties

    def clear(field): # FUNCTION TO CLEAR FIELDS AND MAKE CODE NEAT
        setattr(core, field, None)

    # REMOVE ALL THE FIELDS IF NOTHING IS SELECTED ON SANITIZE
    try:
        if not fields_rem:
            meta_fields = ['title', 'author', 'subject', 'keywords', 'content_status', 'category', 'comments', 'last_modified_by']
            for field in meta_fields:
                clear(field)

            # SETTING THE DATES TO datetime.min as CREATED AND MODIFIED are DATETIME values AND NOT STRINGS
            core.created = datetime(1601, 1, 1)
            core.modified = datetime(1601, 1, 1)
            core.revision = 1 # MANUALLY SETTING it TO 1 as it expects POSITIVE INTEGER and NOT NONE
        
        # REMOVE ONLY WHATS CHOSEN
        else:
            for field in fields_rem:
                if hasattr(core, field):
                    if field in ["created", "modified", "revision"]:
                        core.created = datetime(1601, 1, 1)
                        core.modified = datetime(1601, 1, 1)
                        core.revision = 1
                    else:
                        clear(field)

    except Exception as e:
        print(e) # DEBUG statement
        
    
    # SAVING BACK OUTPUT
    doc.save(out_path)
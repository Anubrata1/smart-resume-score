import fitz  # PyMuPDF
import docx

def parse_resume(file):
    filename = file.filename.lower()
    
    if filename.endswith('.pdf'):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    elif filename.endswith('.docx'):
        doc = docx.Document(file)
        text = "\n".join([p.text for p in doc.paragraphs])
        return text

    else:
        return ""

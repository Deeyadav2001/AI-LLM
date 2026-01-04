

PDF_PATH = r"data/Business-Intelligence-notes.pdf"

from pypdf import PdfReader
import os

def load_pdf_text(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    reader = PdfReader(pdf_path)
    pages_text = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            pages_text.append(text)

    return pages_text




#if pdf is scanned images pdf then this technique 



#def load_pdf_with_ocr(pdf_path):
    #images = convert_from_path(pdf_path)
    #text_pages = []

    #for i, img in enumerate(images):
    #    text = pytesseract.image_to_string(img)
    #    text_pages.append(text)

    #return text_pages


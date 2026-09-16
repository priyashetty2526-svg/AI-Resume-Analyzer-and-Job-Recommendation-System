from pypdf import PdfReader
from docx import Document


def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def extract_text_from_docx(file):
    document = Document(file)
    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_text(file):
    file_name = file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(file)

    elif file_name.endswith(".docx"):
        return extract_text_from_docx(file)

    else:
        raise ValueError("Only PDF and DOCX files are supported.")
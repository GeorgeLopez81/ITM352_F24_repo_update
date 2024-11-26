from docx import Document

def test_docx():
    doc = Document()
    doc.add_paragraph("Hello, this is a test paragraph.")
    doc.save("test.docx")

test_docx()

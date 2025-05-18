from converter_factory import PDFtoDOCXFactory, DOCXtoTXTFactory
from decorators import LoggingDecorator

def main():
    # Convert PDF → DOCX
    pdf_factory = PDFtoDOCXFactory()
    pdf_converter = LoggingDecorator(pdf_factory.create_converter())
    pdf_converter.convert("example.pdf", "example.docx")

    # Convert DOCX → TXT
    docx_factory = DOCXtoTXTFactory()
    txt_converter = LoggingDecorator(docx_factory.create_converter())
    txt_converter.convert("example.docx", "example.txt")

if __name__ == "__main__":
    main()

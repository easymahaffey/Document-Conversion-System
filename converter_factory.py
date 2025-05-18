from abc import ABC, abstractmethod
from pdf2docx import Converter
import docx
import os

class DocumentConverter(ABC):
    @abstractmethod
    def convert(self, input_path: str, output_path: str):
        pass

class PDFtoDOCXConverter(DocumentConverter):
    def convert(self, input_path: str, output_path: str):
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"{input_path} does not exist")
        cv = Converter(input_path)
        cv.convert(output_path)
        cv.close()

class DOCXtoTXTConverter(DocumentConverter):
    def convert(self, input_path: str, output_path: str):
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"{input_path} does not exist")
        doc = docx.Document(input_path)
        with open(output_path, 'w', encoding='utf-8') as txt_file:
            for para in doc.paragraphs:
                txt_file.write(para.text + '\n')

class ConverterFactory(ABC):
    @abstractmethod
    def create_converter(self) -> DocumentConverter:
        pass

class PDFtoDOCXFactory(ConverterFactory):
    def create_converter(self) -> DocumentConverter:
        return PDFtoDOCXConverter()

class DOCXtoTXTFactory(ConverterFactory):
    def create_converter(self) -> DocumentConverter:
        return DOCXtoTXTConverter()

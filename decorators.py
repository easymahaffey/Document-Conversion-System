from converter_factory import DocumentConverter

class ConverterDecorator(DocumentConverter):
    def __init__(self, converter: DocumentConverter):
        self._converter = converter

    def convert(self, input_path: str, output_path: str):
        self._converter.convert(input_path, output_path)

class LoggingDecorator(ConverterDecorator):
    def convert(self, input_path: str, output_path: str):
        print(f"[LOG] Converting: {input_path} → {output_path}")
        super().convert(input_path, output_path)
        print(f"[LOG] Conversion complete.")

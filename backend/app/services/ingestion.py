from pathlib import Path
from pypdf import PdfReader
from docx import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

class DocumentIngestion:

    def extract_text(
        self,
        file_path: str
    ):

        suffix = (
            Path(file_path)
            .suffix
            .lower()
        )

        if suffix == ".pdf":
            return self.extract_pdf_text(
                file_path
            )

        elif suffix == ".docx":
            return self.extract_docx_text(
                file_path
            )

        else:
            raise ValueError(
                f"Unsupported file type: {suffix}"
            )

    def extract_pdf_text(
            self,
            file_path: str
    ):
        reader = PdfReader(
            file_path
        )

        text = ""

        for page in reader.pages:
            page_text = (
                page.extract_text()
            )

            if page_text:
                text +=(
                    page_text
                    + "\n"
                )
        return text
    
    def extract_docx_text(
        self,
        file_path: str
    ):

        doc = Document(file_path)

        text = "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
        )

        return text    

    def chunk_text(
            self,
            text,
            chunk_size = 600,
            chunk_overlap = 100
    ):
        splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n','\n','.'," ",""],
            chunk_size = chunk_size,
            chunk_overlap = chunk_overlap)

        chunks = splitter.split_text(
                text
            )
    
        return chunks
    
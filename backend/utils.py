import io
import pdfplumber
import docx

def chunk_text(text, chunk_size, overlap) -> list:
    """
    chunk the text
    """
    if len(text) <= chunk_size:
        return [text]
    chunks, start = [], 0
    while start < len(text):
        end = start+ chunk_size
        chunks.append(text[start:end])
        start = end-overlap
    return chunks

def extract_text(file_bytes, ext) -> str:
    """
    extract the text
    """
    if ext == "pdf":
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            return "\n".join([p.extract_text() or "" for p in pdf.pages])
    elif ext in ("docx", "doc"):
        doc = docx.Document(io.BytesIO(file_bytes))
        return "\n".join([p.text for p in doc.paragraphs])
    elif ext in ("txt", "md"):
        return file_bytes.decode(errors="ignore")
    return ""

import pdfminer.high_level
import io

def extract_resume_text(uploaded_file):
    file_type = uploaded_file.type
    text = ""

    if file_type == "application/pdf":
        output = io.StringIO()
        pdfminer.high_level.extract_text_to_fp(uploaded_file, output)
        text = output.getvalue()
    elif file_type == "text/plain":
        text = uploaded_file.read().decode("utf-8")
    else:
        text = "Unsupported file type."

    return text

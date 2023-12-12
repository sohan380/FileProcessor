import PyPDF2
import os


def comp_pdfs(folder_path):
    # Get all files in the Input folder
    files = os.listdir(folder_path)
    for filename in files:
        if filename.endswith(".pdf"):
            full_filename = os.path.join(folder_path, filename)
            
            reader = PyPDF2.PdfReader(full_filename)
            writer = PyPDF2.PdfWriter()
            
            for page in reader.pages:
                page.compress_content_streams()
                writer.add_page(page)
            
            with open(os.path.join(folder_path, "compressed_" + filename), "wb") as f:
                writer.write(f)

comp_pdfs("Input")

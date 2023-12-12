# import PyPDF2
# import os

# merger = PyPDF2.PdfMerger()
# files = os.listdir("Input")

# for file in os.listdir(os.curdir):
#     if file.endswith(".pdf"):
#         merger.append(file)

# merger.write("combined.pdf")

import PyPDF2
import os

def merge_pdfs(folder_path):
  merger = PyPDF2.PdfMerger()
  for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
      filepath = os.path.join(folder_path, filename)
      merger.append(filepath)
  output_filepath = os.path.join(folder_path, "combined.pdf")
  merger.write(output_filepath)

# Specify the folder path containing your PDFs
folder_path = os.path.join(os.getcwd(), "Input")

# Merge the PDFs
merge_pdfs("Input")

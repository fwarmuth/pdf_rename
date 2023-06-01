from glob import glob
import os
from pdfrw import PdfReader
import click
tqdm = lambda x: x


dir = "data/papers"

for pdf in glob(os.path.join(dir, "*.pdf")):
    title = PdfReader(pdf).Info.Title
    # remove braces and brackets
    title = title.replace("(", "").replace(")", "").replace("[", "").replace("]", "")
    print(f"{pdf} - {title}")
    # rename the file
    os.rename(pdf, os.path.join(dir, f"{title}.pdf"))

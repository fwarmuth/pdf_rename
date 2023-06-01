import click
from glob import glob
from tqdm import tqdm
import os
from pdfrw import PdfReader

def extract_title(path, no_confirm, dry_run):
    """Extract the title of a PDF"""
    # Check if path is a directory
    if not os.path.isfile(path):
        for pdf in tqdm(glob(os.path.join(path, "*.pdf"))):
            extract_title(pdf, no_confirm, dry_run)
    try:
        title = PdfReader(path).Info.Title
        # Remove braces and brackets
        title = title.replace("(", "").replace(")", "").replace("[", "").replace("]", "")
        # Remove space and replace with underscore
        title = title.replace(" ", "_")
        # Remove forward slash and colon and replace with underscore
        title = title.replace("/", "_").replace(":", "_")

        # Create a new path
        title = os.path.join(os.path.dirname(path), title)

        if no_confirm:
            if not dry_run:
                os.rename(path, f"{title}.pdf")
        else:
            click.confirm(f"Rename {path} to {title}.pdf?", abort=True)
            if not dry_run:
                os.rename(path, f"{title}.pdf")
    except:
        print(f"Skipping {path}.")

@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--no-confirm", is_flag=True, help="Don't ask for confirmation")
@click.option("--dry-run", is_flag=True, help="Don't rename files")
def main(path, no_confirm, dry_run):
    extract_title(path, no_confirm, dry_run)


if __name__ == "__main__":
    main()
import os
import json
import urllib.parse

REPO_URL = "https://github.com/Chret237/site-du-zero-old-pdf/blob/master/"

def get_pdf_files(directory):
    return [f for f in os.listdir(directory) if f.lower().endswith(".pdf")]

def make_entry(filename):
    url_filename = urllib.parse.quote(filename)
    return {
        "title": os.path.splitext(filename)[0].replace("_", " "),
        "filename": filename,
        "url": f"{REPO_URL}{url_filename}",
        "path": filename,
        "size_bytes": os.path.getsize(filename),
        "author": "Unknown",
        "description": "",
        "tags": [],
        "publication_year": "Unknown"
    }

def main():
    pdfs = get_pdf_files(".")
    entries = [make_entry(pdf) for pdf in pdfs]
    with open("readers.json", "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    print(f"Generated readers.json with {len(entries)} entries.")

if __name__ == "__main__":
    main()
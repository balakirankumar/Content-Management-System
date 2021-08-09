import secrets
import os
from CMS import app

def download_pdf(file):
    random_hex=secrets.token_hex(8)
    filename=random_hex+os.path.splitext(file.filename)[-1]
    print(filename)
    file.save(os.path.join(app.root_path,'static/documents/',filename))
    return filename

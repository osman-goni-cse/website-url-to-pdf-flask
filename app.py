# from crypt import methods
import imp
from urllib.parse import urlparse
from flask import Flask, render_template, request
import pdfkit as pdf
import os
from urllib.parse import urlparse
from pathlib import Path

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
  if(request.method == 'POST'):
    # print(request.form['website-url'])
    url = request.form['website-url']
    print(url)
    print(type(url))
    # print(os.path.basename(filename.path))
    p = Path(url)
    print(p.stem)
    filename = str(p.stem)+".pdf"

    print(filename)
    
    # pdf.from_url(url, 'website.pdf')
    pdf.from_url(url, filename)

  return render_template('index.html')
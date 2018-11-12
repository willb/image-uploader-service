#!/usr/bin/env python

# some file uploading code adapted from Flask documentation

from flask import Flask, redirect, request, url_for
import base64

from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    f = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if f.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if f and allowed_file(f.filename):
        filename = secure_filename(f.filename)
        # fixme
        return "<!doctype html><title>got your file</title><p>received file %s</p>" % filename
  return '''
    <!doctype html>
    <title>Upload an image</title>
    <h1>Upload an image</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
  app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
  app.logger.setLevel(0)
  app.run(host='0.0.0.0', port=8080)
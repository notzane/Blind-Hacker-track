import os
from flask import Flask, request, redirect, url_for, make_response
from werkzeug.utils import secure_filename
from flask import send_from_directory
from flask import render_template
from flask import flash
import unbias

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSION = 'pdf'


application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
application.secret_key = "super secret key"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == ALLOWED_EXTENSION

@application.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            outfile = "resume_unbiased.pdf"
            path = os.path.join(application.config['UPLOAD_FOLDER'], filename)
            outpath =os.path.join(application.config['UPLOAD_FOLDER'], outfile)
            file.save(path)
            if(request.form['filter'] == "Remove Name"):
                unbias.unbias(path, outpath, False)
            else:
                unbias.unbias(path, outpath, True)
            return send_from_directory(directory="uploads", filename=outfile, as_attachment=True)

    return render_template('solid/index.html')

@application.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(application.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    application.run(debug=True)

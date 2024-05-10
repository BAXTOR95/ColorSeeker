import os
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap5
from colors_extractor import process_image
from datetime import datetime

bootstrap = Bootstrap5()
app = Flask(__name__, template_folder='web/templates')
bootstrap.init_app(app)

# configure upload folder
UPLOAD_FOLDER = 'uploads'

# create the folder if it doesn't exist
os.makedirs(os.path.join(app.instance_path, UPLOAD_FOLDER), exist_ok=True)

PROD = True if os.environ.get('PROD', False) == 'True' else False


@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_name = secure_filename(file.filename)
            file_path = os.path.join(app.instance_path, UPLOAD_FOLDER, file_name)
            file.save(file_path)
            # Process the image and extract colors
            colors = process_image(file_path)
            # Generate URL for the uploaded file
            image_url = url_for('uploaded_file', filename=file_name)
            return render_template('index.html', colors=colors, image_path=image_url)
    return render_template('index.html', colors=None, image_path=None)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(app.instance_path, UPLOAD_FOLDER), filename)


if __name__ == '__main__':
    app.run(debug=not PROD)

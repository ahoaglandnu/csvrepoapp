from flask import Flask, render_template, request, redirect, url_for, send_file, flash 
from werkzeug import secure_filename 
from flask_sqlalchemy import SQLAlchemy
import os
import csv
import io

app = Flask(__name__)

db_path = os.path.join(os.path.dirname(__file__), 'csvtodbapp.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['ALLOWED_EXTENSIONS'] = set(['csv'])
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 0.1
app.secret_key = "temp for dev"

db = SQLAlchemy(app)

class CsvFile(db.Model):
	record_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(300))
	data = db.Column(db.LargeBinary)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# Home page
@app.route('/')
def index():
	return render_template('index.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        newFile = CsvFile(name=filename, data=file.read())
        db.session.add(newFile)
        db.session.commit()
        flash('Your file was successfully uploaded', 'success')
        return redirect(url_for('dashboard'))
    else:
    	return redirect(url_for('error'))

# Error page for non-csv files
@app.route('/error')
def error():
    return render_template('error.html')

# Dashboard of CSV Files
@app.route('/dashboard')
def dashboard():
	dashboard = CsvFile.query.all()
	return render_template('dashboard.html', title="CSV Files", dashboard=dashboard)

#Individual CSV File for download
@app.route('/file/<int:record_id>/', methods=['GET'])
def file(record_id):
 	myFiles = db.session.query(CsvFile).filter(CsvFile.record_id == record_id).first()
 	filename = myFiles.name 
 	return send_file(io.BytesIO(myFiles.data), attachment_filename=myFiles.name, as_attachment=True)

if __name__ == '__main__':
	app.run(debug=True)
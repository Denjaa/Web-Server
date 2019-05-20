import os
from source.application import app, ALLOWED_EXTENSIONS
from flask import Flask, request, render_template, redirect, send_file
from werkzeug.utils import secure_filename
import datetime, pandas as pd
from source.handler import CSV

def allowed_extensions(filename):
	return '.' in filename and filename.rsplit('.')[-1].lower() in ALLOWED_EXTENSIONS

def runScripts(input_file):
	extension = str(input_file).split('.')[-1]

	if extension.endswith('csv'):
		csv = CSV()
		fOut = str(input_file.split('\\')[-1]).split('.')[0]
		result = csv.GBI(inputFile = input_file, outputFile = fOut, root = os.getcwd())

	return result

@app.route('/base', methods = ['GET'])
def base():
	return render_template('base.html')

@app.route('/', methods = ['GET', 'POST'])
def process():
	global result
	
	if request.method == 'GET':
		return render_template('upload.html')
	
	elif request.method == 'POST':

		inputFile = request.files['file-name']

		if inputFile.filename == '':
			return redirect(request.url)

		if inputFile and allowed_extensions(inputFile.filename):
			namefix = str(inputFile.filename).split('.')
			unique_name = namefix[0] + '_' + str(datetime.datetime.now().isoformat()) + '.' + namefix[-1]
			unique_name = secure_filename(unique_name)
			inputFile.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_name))

			result = runScripts(input_file = (str(os.getcwd()) + '\\uploads\\' + unique_name))

			return render_template('download.html', value = result)

	return "HAHAH"

@app.route('/download', methods = ['POST'])
def download():
	fileName = result.split('\\')[-1]
	
	return send_file(result, mimetype = 'text/csv', attachment_filename = str(fileName), as_attachment = True)


if __name__ == "__main__":
    app.run(debug = True)

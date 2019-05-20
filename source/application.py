from flask import Flask
import os
from .flask_celery import make_celery

if not os.path.exists(os.path.join(os.getcwd() + '\\uploads')):
	os.makedirs(os.path.join(os.getcwd() + '\\uploads'), exist_ok = True)

if not os.path.exists(os.path.join(os.getcwd() + '\\downloads')):
	os.makedirs(os.path.join(os.getcwd() + '\\downloads'), exist_ok = True)	

ALLOWED_EXTENSIONS = set(['csv', 'xlsx', 'xls', 'txt', 'pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + '\\uploads'
app.config.update(CELERY_BROKER_URL='amqp://localhost:5672', CELERY_RESULT_BACKEND='db+sqlite:///results.sqlite')

celery = make_celery(app)

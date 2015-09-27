# project/fuzzy/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, url_for, redirect, request, abort, Response
from werkzeug import secure_filename
import json
import os
import pandas as pd
from project.worker.tasks import app, find_match
import csv
import urllib.request
import requests
import re
import ast




################
#### config ####
################


fuzzy_blueprint = Blueprint('fuzzy', __name__, template_folder='templates')
path = os.path.dirname(os.path.abspath(__file__))


################
#### routes ####
################

@fuzzy_blueprint.route('/')
def index():
    return render_template('index.html')


# @fuzzy_blueprint.route('/<page>')
# def show(page):
#     try:
#         return render_template('%s.html' % page)
#     except TemplateNotFound:
#         abort(404)    


@fuzzy_blueprint.route('/upload', methods=['POST'])
def upload():
	
	file = request.files['file']
	filename = secure_filename(file.filename)
	file.save(os.path.join(path, 'file_upload/'+filename))
	
	country = request.form.get("country")
	territory = request.form.get("territory")

	# print ("country: {}".format(country))
	# print ("territory: {}".format(territory))

	country = country.lower()
	territory = ast.literal_eval(territory)

	# print ("joined territory: {}".format(type(territory)))
	
	result = {}
	result['i'] = request.form.get("i")
	result['job_id'] = str(find_match.apply_async((filename,country,territory)))

	return json.dumps(result), 200

@fuzzy_blueprint.route('/result/<job_id>', methods=['GET'])
def result(job_id):
	
	result = app.AsyncResult(job_id)
	state = result.state
	
	status = 202
	if state == "SUCCESS" or state == "FAILURE" or state == "REVOKED":
		status = 200

	return state, status	

@fuzzy_blueprint.route('/cancel', methods=['POST'])
def cancel():
	# print("CANCELLLLLLLLLLLLLLLLLl!!!!!!!!!!!!!!!!!!")
	data = request.get_json()

	print("data:{}".format(data))

	for job_id in data["job_ids"]:
		app.control.revoke(job_id, terminate=True)

	return "CANCELLED", 200		



@fuzzy_blueprint.route('/download/<filename>')
def generate_csv(filename):

	data = pd.read_csv(os.path.join(path, 'file_download/'+"_".join(filename.split(" "))))
	columns = (list(data.columns.values))


	def generate():
		yield ','.join(columns) + '\n'
		for row in data.iterrows():
			yield ','.join((re.sub(r"\bnan\b", "", "\""+str(row[1][column]))+"\"" for column in columns)) + '\n'

	return Response(generate(), mimetype='text/csv')


@fuzzy_blueprint.route('/send/<filename>')
def send(filename, score):

		pass
			




        
    

	



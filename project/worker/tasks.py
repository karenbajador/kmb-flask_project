from celery import Celery
from project.fuzzy.fuzzy import Fuzzy
from project.fuzzy.api import FuzzyAPI
import os

app = Celery('tasks')
app.config_from_object(os.environ['APP_SETTINGS'])



@app.task(name='project.worker.tasks.find_match')
def find_match(filename, country, territory):
	
	find_match.update_state(state='UPLOADING',
                meta={})
	f = Fuzzy(filename,country,territory)
	

	find_match.update_state(state='FINDING MATCHES',
                meta={})
	proceed = f.start()
	# proceed = f.start_test()
	
	

	if proceed:
		find_match.update_state(state='SUCCESS',
                meta={})
		


@app.task(name='project.worker.tasks.send_to_crm')
def send_to_crm(filename, tag, score, country):

	send_to_crm.update_state(state='SENDING',
                meta={})
	f = FuzzyAPI(filename,tag, score, country)
	success = f.send_to_crm()
	if success:
		send_to_crm.update_state(state='SUCCESS',
                meta={})

	
	



	








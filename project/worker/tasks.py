

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
BROKER_URL = 'redis://127.0.0.1:6379/0'


from celery import Celery
import time
from project.fuzzy.fuzzy import Fuzzy


app = Celery('tasks', backend=CELERY_RESULT_BACKEND, broker=BROKER_URL)

@app.task(name='project.worker.tasks.add')
def return_states():
	statuses = ['UPLOADING','FINDING MATCHES', 'DONE']
	for status in statuses:
		return_states.update_state(state=status,
                meta={})
		time.sleep(5)


@app.task(name='project.worker.tasks.find_match')
def find_match(filename, country, territory):
	find_match.update_state(state='UPLOADING',
                meta={})
	print("************************" + app.AsyncResult(find_match.request.id).state)
	time.sleep(5)

	print("INSIDE FIND MATCH ----------------------------------------------->")
	print("filename {}".format(filename))
	print("territory {}".format(territory))
	print("country {}".format(country))

	f = Fuzzy(filename,country,territory)
	find_match.update_state(state='FINDING MATCHES',
                meta={})
	print("************************" + app.AsyncResult(find_match.request.id).state)

	proceed = f.start()
	

	if proceed:
		find_match.update_state(state='PREPARING FILE',
                meta={})
		print("************************" + app.AsyncResult(find_match.request.id).state)
		f.save()
		find_match.update_state(state='SUCCESS',
                meta={})
		print("************************" + app.AsyncResult(find_match.request.id).state)



	
	



	








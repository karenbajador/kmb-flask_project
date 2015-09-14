from tasks import return_states
import time


result = return_states.delay()

print (result.state)
time.sleep(5)
print (result.state)
time.sleep(5)
print (result.state)
time.sleep(5)
print (result.state)
time.sleep(5)	
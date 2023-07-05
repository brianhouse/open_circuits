from aio_helper import *

    
while True:    
    data = pull_data("button-press", now()-3600, now())
    value = data[-1]['value']
    print(value)

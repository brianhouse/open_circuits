import urllib2
import json
import time
from credentials import *

def pull_data(feed, start_time, end_time):
    print("Pulling data... ")
    url = "https://io.adafruit.com/api/v2/" + AIO_USERNAME + "/feeds/" + feed + "/data?start_time=" + str(start_time) + "&end_time=" + str(end_time)
    request = urllib2.Request(url, headers={"X-AIO-Key": AIO_KEY})
    data = []
    try:
        response = urllib2.urlopen(request)
        results = json.loads(response.read())
        time.sleep(2) # avoid going over rate limits        
        start_t = results[-1]['created_epoch']
        for item in results:
            data.append({'time': item['created_epoch'] - start_t, 'value': float(item['value'])})
        data.sort(key=lambda d: d['time'])
        print("--> success")
        return data
    except Exception as e:
        print(e)
    return []


def now():
    return int(time.time()) 

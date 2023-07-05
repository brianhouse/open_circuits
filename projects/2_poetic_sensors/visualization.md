# Data Visualization Basics


## Setup

Open a new Processing sketch in Python mode and save it. Then, download [aio_helper.py](poetic_sensors_demo/aio_helper.py) and add it to the sketch.

In addition, create a new tab by clicking on the down arrow next to the open filename, call it "credentials.py", and include the following:

```py
AIO_USERNAME = "h0use"
AIO_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # <-- your key here
```

## Pulling Data

In your sketch, try the following:

```py
from aio_helper import *

data = pull_data("hall-sensor", now()-360000, now())
```
You should see this in your console:
```
Pulling data...
--> success
```

The `pull_data()` function connects to AIO and downloads all the sensor data between the start time and the end time. Here, the start time is "now()-360000", which means the present time minus 360,000 seconds, which is 10 hours. The end time is simply "now". So every time this sketch is run, it will pull the most recent 10 hours worth of data.

`now` lets us work with relative time in this way. But we can also give the function absolute timestamps. Use this site to convert from "human" dates to a timestamp that the computer can understand: https://www.epochconverter.com

**Remember not to pull data more than every couple seconds.** More on this later.

## Data Format

The data that results is a list of dictionaries, each with two fields: `time` and `value`. For example:

```py
[   {'time': 0, 'value': 0.01416361},
    {'time': 3, 'value': 0.01196581},
    {'time': 7, 'value': 0.01343101},
    {'time': 10, 'value': 0.01440781},
    {'time': 14, 'value': 0.01367521},
    {'time': 17, 'value': 0.01318681},
    {'time': 21, 'value': 0.01391941},
    {'time': 24, 'value': 0.01343101},
    ...
]
```
`time` is the number of seconds since the start time that you supplied to `pull_data()`. `value` is the value that was posted by the ESP32.

## `map()`

The most basic approach to visualizing this data is to represent it as a graph across the canvas. To do that, we'll need to convert the `time` of the data—when each one was posted—to an x-coordinate on the canvas. Likewise, we'll need to convert the `value` to a y-coordinate on the canvas.

The problem here is that the timespan in number of seconds of our data does not correspond to the width of the canvas. Likewise, the range of the values is not the same as the height of the canvas.

To make this conversion, we use the [`map()`](https://py.processing.org/reference/map.html) function. `map()` takes an input value and its initial range and rescales it to our desired range. It is incredibly useful!

`map(input_value, input_min, input_max, output_min, output_max)`

To begin, let's get the start time and end time of the data. The start time is easy—it's 0. The end time we can get using list syntax:
```py
from aio_helper import *

data = pull_data("hall-sensor", now()-360000, now())

min_time = 0
max_time = data[-1]['time']  # time field of the last dictionary in the list
```

Now we need the min and max values of the data. This highly depends on the sensor and how you've coded the ESP32—it could be 0–1, or 0–4095, or some more constrained range in between (you might look on AIO and the auto-detected range to come up with some good parameters).

```py
from aio_helper import *

data = pull_data("hall-sensor", now()-360000, now())

min_time = 0
max_time = data[-1]['time']  # time field of the last dictionary in the list
min_value = 0
max_value = 4095
```

Once we have these parameters, we can iterate through all of our data with a `for` loop and use `map()` to rescale it to useable coordinates:


```py
from aio_helper import *

data = pull_data("hall-sensor", now()-360000, now())

min_time = 0
max_time = data[-1]['time']  # time field of the last dictionary in the list
min_value = 0
max_value = 4095

for datapoint in data:
    x = map(datapoint['time'], min_time, max_time, 0, width)
    y = map(datapoint['value'], min_value, max_value, height, 0)
```

Notice that we're scaling our x-coordinates from `0` to `width`, the full canvas. This is reversed for the y-coordinates ... why? Since Processing puts 0,0 in the upper-left, but we want higher values to be higher vertically, we flip the range.

Let's just put a point at each x, y coordinate, and use `strokeWeight()` ahead of time to give it some volume. And don't forget to make a canvas!:

```py
from aio_helper import *

data = pull_data("hall-sensor", now()-360000, now())

min_time = 0
max_time = data[-1]['time']  # time field of the last dictionary in the list
min_value = 0
max_value = 4095

size(640, 480)
background(255)
strokeWeight(5)
for datapoint in data:
    x = map(datapoint['time'], min_time, max_time, 0, width)
    y = map(datapoint['value'], min_value, max_value, height, 0)
    point(x, y)
```

![](img/v1_points.png)

Note that if there are no data, you will get an error, and that finding the start and end times might be a little tricky—use the filters on AIO and https://www.epochconverter.com!

Here's a slightly more elaborate variation using `curveVertex`s instead:

```py
#...
size(640, 480)
background(255)
strokeWeight(5)
beginShape()
for datapoint in data:
    x = map(datapoint['time'], min_time, max_time, 0, width)
    y = map(datapoint['value'], min_value, max_value, height, 0)
    curveVertex(x, y)
endShape()
```

![](img/v2_vertex.png)

Now, this conforms to our basic understanding of a graph. But using any of our prior lessons in Processing, we could make something more interesting happen using the same data:

![](img/v3_split.png)

This is a ridiculous example, but how and why you choose to visualize your data is part of the exercise.

<!--
```py
from aio_helper import *

size(400, 400)
source = loadImage("robot_over.png")
source_2 = loadImage("lion_over.png")

data = pull_data("hall-sensor", 1644308086, 1644390886)    
# print(data)

min_time = 0
max_time = data[-1]['time']  # time field of the last dictionary in the list
min_value = 30
max_value = 90

background(255)

ts = []
vs = []
for datapoint in data:
    t = map(datapoint['time'], min_time, max_time, 0, height)
    v = map(datapoint['value'], min_value, max_value, 0, width)    
    ts.append(t)
    vs.append(v)


for y in range(height):
    index = 0
    while index < len(ts) - 1 and ts[index] < y:
        index += 1
    for x in range(width):
        pixel_1 = source.get(width-x, y)
        r_1 = red(pixel_1)
        g_1 = green(pixel_1)
        b_1 = blue(pixel_1)

        pixel_2 = source_2.get(x, y)
        r_2 = red(pixel_2)
        g_2 = green(pixel_2)
        b_2 = blue(pixel_2)        

        value = vs[index]
        if x < value:
            stroke(r_1, g_1, b_1)
        else:
            stroke(r_2, g_2, b_2)               
        point(x, y)
```
-->

## Working with Events

With many applications, rather than tracking continuously changing values, you are only posting data from a sensor to mark the time that a particular kind of event occurs—every time someone walks through a door, for example.

Your ESP32 code might contain threshold code like this:
```py
if value < threshold:
    if triggered is False:
        triggered = True
        post_data("door", 1)
else:
    triggered = False    
```

This means that every value you post to Adafruit will be a `1`, so they aren't very useful. But the _timestamps_ are useful.

This works similarly to the above example, but it's even more simple.

Like before, let's first determine a start time and an end time for our data. We're going to look at data over the last 24-hour period:

<!-- # data = pull_data("hall-sensor", 1644308086, 1644390886)# print(data)

data = []
for i in range(50):
    data.append({'time': random.randint(0, 100)})
data.sort(key=lambda d: d['time']) -->


```py
from aio_helper import *

data = pull_data("switch", now()-(24*3600), now())

min_time = 0
max_time = data[-1]['time']  # time field of the last dictionary in the list
```

Next, we only need to map the times:
```py
from aio_helper import *

data = pull_data("switch", now()-360000, now())

min_time = 0
max_time = data[-1]['time']  # time field of the last dictionary in the list

size(640, 480)
background(255)
strokeWeight(5)
for datapoint in data:
    x = map(datapoint['time'], min_time, max_time, 0, width)
    point(x, height/2)
```

![](img/v4_threshold.png)

...or, to express the passage of time in a different way using the circle equation:
```py
size(640, 480)
background(255)
for datapoint in data:
    a = map(datapoint['time'], min_time, max_time, 0, 360)
    x = width/2 + cos(radians(a)) * 200
    y = height/2 + sin(radians(a)) * 200
    strokeWeight(1)
    stroke(180)
    line(width/2, height/2, x, y)
    strokeWeight(5)
    stroke(0)
    point(x, y)
```

![](img/v5_clock.png)

## Real-Time Data

An alternative approach is to constantly pull the most recent data point and create a visualization based on that.

In this case, we'll need to reformat our sketch in order to use `setup()` and `draw()`. In addition, we'll need to use variables to set up a timer mechanism so that we can pull new data every so often—let's say every 5 minutes:

```py
from aio_helper import *

def setup():
    global start_time, value, data
    size(800, 600)
    background(255)
    start_time = 0
    value = 0
    data = None

def draw():
    global start_time, value
    elapsed_time = time.time() - start_time
    if elapsed_time > 5*60:
        start_time = elapsed_time
        # update data

    #... draw stuff ...
```

Under this conditional that runs every 5 minutes, we will pull the data and get the most recent point:

```py
def draw():
    global start_time, value, data
    elapsed_time = time.time() - start_time
    if elapsed_time > 15:
        start_time = elapsed_time

        data = pull_data("temperature", now()-3600, now())
        last_data_point = data[-1]
        value = data['value']

    #... draw stuff ...
```

Now, we can do something with that value. Like ... control the number of agents in a simulation, or the speed of an animation, or the color of a big rectangle:

```py
def draw():
    global start_time, value, data
    elapsed_time = time.time() - start_time
    if elapsed_time > 15:
        start_time = elapsed_time

        data = pull_data("temperature", now()-3600, now())
        last_data_point = data[-1]
        value = data['value']

        min_value = 30 # degrees fahrenheit
        max_value = 80

    # map our temperature range to 0–1
    hotness = map(value, min_value, max_value, 0, 1)

    # interpolate from a cold color to a hot color depending on that mapped value
    cold_color = color(0, 0, 255)
    hot_color = color(255, 0, 0)
    c = lerpColor(cold_color, hot_color, hotness) #

    noStroke()
    fill(c)
    rect(0, 0, width, height)
```

This simple example just provides a color field matching the temperature at the site of the sensor. It also demonstrates another useful function, [`lerpColor()`](https://py.processing.org/reference/lerpColor.html), which takes two colors as arguments and outputs a new one. This new color is somewhere in between, depending on a third argument that ranges between 0 and 1.

![](img/v6_temp.png)

# Micropython

[Micropython](https://micropython.org) is a programming language based on Python—one of the most popular and powerful interpreted languages that is in use today. The only difference between Micropython and Python is that Micropython is optimized to run on microcontrollers like the ESP32, which excludes some advanced features. Micropython is similar to the Arduino programming language, although it is more elegant and easy to learn (at the cost of being somewhat slower).


## Variables and Operators

Variables in Micropython are special words that serve as "containers" for values that may change. They can be numbers, text (aka "strings"), booleans (aka `True` or `False`), lists of other variables, or None if they hold nothing at all. To assign a variable, you use the `=` sign.

```py
x = 4     					# assign a number to a variable
name = "Brian" 					# strings
activated = True				# boolean
favorite_numbers = [2, 4, 6, 17]	 	# a list of numbers
result = None					# a placeholder
```

Just like in math, you can operate on variables and assign them new values:
```py
x *= 2  		# multiply x by 2
x += 1 			# add 1 to x
x %= 10 		# set x to its remainder when divided by 10 (modulo)
x = y + z		# x is the sum of y and z
x = y / z		# x is y divided by z
```

You can also compare variables. These operators result in either `True` or `False` for use in a conditional statement, which we'll get to next.
```py
a == b			# a is the same as b .... (note the double =)
a != b 			# a is not the same as b
a > b 			# greater than
a < b 			# lesser than
a >= b 			# greater than or equal to
a <= b 			# lesser than or equal to
```

## Conditionals

### `if`

You can use those comparison operators in a conditional statement, which looks like this:
```py
if a > b:
    do stuff!
```
This reads, "if a is greater than b, do stuff!" Note the colon after the if statement, as well as the indentation on the next line. Micropython doesn't use brackets {} like other programming languages, so the indentation is really important!

That's especially the case when you add an `else` statement:
```py
if a > b:
    do stuff!
else:
    do other stuff!
```
In this case, if `a` _isn't_ greater than `b`, the code performs an alternative.


### `while` and `for` loops

Another type of conditional is a `while` loop. This does things over and over until the condition is no longer valid. For example:
```py
a = 0
while a < 10:
    print(a)
    a += 1 
```

This code first creates a variable, `a`, and sets it to 0. As long as `a` is less than 10, it prints out the value and then increments the value by 1. As soon as it hits 10, the loop is no longer valid and the code moves on. Note the colon and the indentation.

`print()` is a _function_ also a function that prints a variable or a text string to the console (in our case, the output within Thonny). `print()` can print multiple variables or text strings by separating them with commas. Something like:
```py
print("a", a, "b", b)
```
...will look nice in the Thonny console, because you can use the plotter to look at the labeled numbers graphically.



## Importing functions

To add additional functions to our repertoire, we can use an import statement to bring them in from a module that's already been written, whether we've added that module manually or from the built-in standard library.

For our purposes, we will typically be adding:
```py
from esp_helper import *
```
...to the top of our code, which adds some functions specific to the ESP and our needs in the course. Some of the following functions are dependent on that module.

Not all the available functions are listed here. Those relevant to specific hardware will be referenced in other sections of this guide, and Micropython / Python has tons of functions that you can find referenced online.


## Timing

### `sleep()`

A particularly useful function is `sleep()`, which makes the microcontroller wait a moment. Because sensors and components can't always keep up with the speed of the processor, this is often advisable to use in a loop between reading sensors. Sleep takes a parameter, also known as an argument, which is the number of seconds to wait:
```py
sleep(1) # wait one second
```

### `ticks_ms()`

This returns the number of milliseconds since the microcontroller was powered on. You can use it to determine how much time has elapsed. For example:
```py
start_time = ticks_ms()
while ticks_ms() - start_time < 10000: # wait 10 seconds (10000 milliseconds)
    print("Still waiting...")
    # do other stuff

print("10 seconds have elapsed!")
```

## Indeterminacy

### `random()`

```py
# print a random number between 0 and 1 every second
while True:
    r = random()
    print(r)
    sleep(1)
```


### `randint()`

Returns a random integer.
```py
# print a random integer between 0 and 100 every second
while True:
    r = randint(0, 100)
    print(r)
    sleep(1)
```


### `choice()`

This function returns a random element from a list or tuple (see below).

```py
numbers = 1000, 42, 19, 256  # print one of these numbers every second

while True:
    r = choice(numbers)
    print(r)
    sleep(1)
```

## Scaling values

### `map()`

Map is useful for when you have an input range of values that you want to scale to a different output range of values. It takes five parameters—the variable you want to (re)map, the input minimum and maxiumum, and the output minimum and maximum. It returns the rescaled value. In this example, a sensor that returns values from 0 to 4095 is mapped to piezo that plays frequencies from 100 to 1000 Hz.

```py
sensor_value = A2.read()
frequency = map(sensor_value, 0, 4095, 100, 1000)  # scale 0–4095 to 0–10
beeper.freq(frequency)
```


## Casting

In some situations, you want a decimal number to be an integer, or to convert an integer into one with decimals. Or sometimes, you want a number to be understood as text. To convert variables from one type of information to another, we use "casting" functions.

- `int()` convert to integer
- `float()` convert to float / decimal
- `str()` convert to a string / text


## ESP32 pin setup

There are several functions that configure and use the pins on the ESP32.


### Analog pins

The ESP32 has several analog sensor pins, marked A2, A3, A4 (A0, A1, A5 work slightly differently and are best avoided for now). These names are available as variables in Micropython. To read the voltage from one of these pins, we use a "method", which is a function that is attached to a variable with a dot. Like this:

```py
value = A0.read()
```
Here, the ESP32 reads the voltage from the A0 pin and stores it in a new "value" variable.

For the specifics of how and why to use this, check out the [sensors](sensors.md) section.


## Tuples and Lists

In Micropython, you can store multiple items in a single variable. Like this:

```py
fruits = "apple", "banana", "cherry"
```

Each item has an 'index'. The first item is index 0, the second is index 1, and so forth (counting starting with 0 can be confusing at first, but there are reasons why it is ultimately helpful).

Printing out the second item (banana) in a tuple or list, for example, is like this:

```py
print(fruits[1])
```

The difference between a tuple and a list is that lists can change. To define a list instead of a tuple, we put brackets around it.

So this will not work:

```py
small_numbers = 0.001, 0.5, 2
small_numbers[2] = 1.5
```

...but this will:
```py
small_numbers = [0.001, 0.5, 2]    # brackets!
small_numbers[2] = 1.5
```

Additionally, with lists we can add items to the end as we go:
```py
small_numbers = [0.001, 0.5, 2]
small_numbers.append(1.5)
```

Often, this means it's helpful to start with an empty list:
```py
small_numbers = []
```

Tuples and loops can work well with a special kind of loop called a `for` loop:
```py
fruits = "apple", "banana", "cherry"
for fruit in fruits:
    print("Have a", fruit)
```
```
Have a apple
Have a banana
Have a cherry
```


### Digital pins

The ESP32 has several GPIO (General Purpose Input/Ouput) pins that can be inputs or outputs. These are marked 13, 12, 27, 33, 15, 32, 14 (in that order) across the top of the board (note that pin 13 is also attached to an onboard LED).

An input reads whether a circuit is high or low voltage. Before it can be used, the pin has to be configured with the `IN()` function:

```py
my_input = IN(12)     # configure the pin as an input

while True:
    value = my_input.value() # read the value
    print(value)
    sleep(.1)
```

An output turns the pin on or off, meaning that it will put out 3.3v (or not):
```py
my_output = OUT(12)     # configure the pin as an output

while True:
    value = my_output.on()
    sleep(1)
    value = my_output.off()
    sleep(1)
```

You'll see the specifics of how to use these in subsequent sections.

In addition, pins can be configured via [`TOUCH()`](sensors.md#touch), [`TONE()`](piezos.md), and [`NEOPIXELS()`](neopixels.md), which are described in the corresponding sections.



## Generalizing from the examples

The examples in this guide include short code snippets to accomplish a single task. But your programs will likely need to do several things simultaneously. 

Rather than cutting and pasting everything from the examples, make sure that your program has one main loop. This should come last, after your input statement, starting any special sensors, and initializing your pins (in that order). Finally, include a short `sleep()`.

As you go, you'll get a better hang of the syntax.

```py
from esp_helper import *

# start any special sensors
start_wifi()
start_imu()

# initialize pins here
sound = TONE(27)
robot_lights = NEOPIXELS(32)
start_btn = IN(10)
presence = A2



# start the loop
while True:
    do stuff

    sleep(.1) # include a sleep statement
```


## Resetting the ESP32

Note that whenever the ESP32 turns on it will automatically run the code in `main.py`. However, if you disconnect the ESP32 from Thonny while it's not running, you'll need to either unplug and plug it in again or reset it to make the code start. And in some cases, you may just want your code to restart manually. 

In these cases, press the small button on the ES32 Feather board to reset.


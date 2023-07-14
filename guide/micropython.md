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


### `while`

Another type of conditional is a `while` loop. This does things over and over until the condition is no longer valid. For example:
```py
a = 0
while a < 10:
    print(a)
    a += 1 
```

This code first creates a variable, `a`, and sets it to 0. As long as `a` is less than 10, it prints out the value and then increments the value by 1. As soon as it hits 10, the loop is no longer valid and the code moves on. Note that colon and the indentation.

`print()` is a _function_ that prints a variable or a text string to the console (in our case, the output within Thonny). `print()` can print multiple variables or text strings by separating them with commas. Something like:
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

A particularly useful function is `sleep()`, which makes the microcontroller wait a moment. Because sensors and components can't always keep up with the speed of the processor, this is often adviseable to use in a loop between reading sensors. Sleep takes a parameter, which is the number of seconds to wait:
```py
sleep(1) # wait one second
```

### `time()`

On a computer, `time()` returns the number of seconds that have elapsed since January 1st, 1970. However, when a microcontroller like the ESP32 is turned on, it has no idea what the date is. So it will pick an arbitrary number and start counting seconds up from there. You can use it to determine how much time has elapsed. For example:
```py
start_time = time()
while time() - start_time < 10:
    print("Still waiting...")
    # do other stuff

print("10 seconds have elapsed!")
```


## ESP32 pin setup

There are several functions that configure and use the pins on the ESP32.


### Analog pins

The ESP32 has several analog sensor pins, marked A2, A3, A4, and A37 on board (A0, A1, A5 work slightly differently and are best avoided for now). These names are available as variables in Micropython. To read the voltage from one of these pins, we use a "method", which is a function that is attached to a variable with a dot. Like this:

```py
value = A0.read()
```
Here, the ESP32 reads the voltage from the A0 pin and stores it in a new "value" variable.

For the specifics of how and why to use this, check out the [sensors](sensors.md) section.


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

In addition, pins can be configured via [`TOUCH()`](sensors.md#touch) and [`TONE()`](piezos.md).





## Lists


## On the ESP32

keeps running regardless

click the button to reset the program


casting

random, choice

## Exercises

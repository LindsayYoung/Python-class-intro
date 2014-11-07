
Python Class
============
18F Women in Tech & Data Hackathon + Training Day
1hr 15min introduction to Python
----

###Introduction

If you have not used Python before, sign-up for [PythonAnyware](https://www.pythonanywhere.com/). It will run python for you without installing things on your computer. Go ahead and do that while I am talking.

Why learn to code?
* It is fun
* Do things more efficiently
* Valuable career

What is Python?
* Python is a coding language
* You give your computer vary specific instructions
* Like any language, Python has syntax and grammatical rules that you need to follow so your computer knows what you want. The rules can be frustrating because unlike (most)humans, computers will freak out if your punctuation is off or there is unexpected whitespace.
* It is very flexible and you can do things like websites or analyze data and so much more
* Python is an open source language

Open source is awesome!
* Great community, people to help you
* Python (and Ruby) are open source
* Use other, smart people's code- (You don't have to do it all your self.)
* Your projects can be open source too!

###Run code

Python is a free, open source language. For the beginning of the class we are going to use PythonAnywhere to run our code in our browser.
* [PythonAnywhere](https://www.pythonanywhere.com)
1. run a line of code directly in the IPython console (we are using 2.7)
2. make a file and click save and run
3. make a file and  and open the Bash console and type: python the_name_of_your_file.py


You can do many useful things with Python but today, we are going to do something fun. We will be making a "madlibs" it will show us some basics of Python.

I will now sign up for [PythonAnyware](https://www.pythonanywhere.com/).

###Objects

In Python, we work with objects. Thiat means we create, store and change objects in our programs. Useful objects are things like numbers and words. As we continue, we will make much more complex objects, but lets start with the basics. (See the [python documantation](https://docs.python.org/2/library/types.html) if you want to sneek a peek.)

We can also create variables in python. You can think of creating variables as naming objects so you can remember them later and when you call them, they will be ready for you. Variable names can't start with numbers and they can't have spaces.

Let's see a simple example of assigning a variable in the python console:
```
>>> greeting = "Hello"
>>> print(greeting)
Hello
```

In that code, we assigned the value, "Hello" to the variable name greeting. When you make variables, the name always goes to the left and the value that is being represented always goes to the right. We then used the print function to show us the value of greeting.

We can create many objects for our programs that you can think of as numbers and words, but computers need a lot more specificity. So, in this case, we are talking about three types of objects in python.

###Types
* integer- think of this as a whole number; no decimals. You can do math with this type of object but if you need the precision of decimals, say if you are doing division, don't use this because the computer will keep rounding the numbers to make them whole.
* float- think of this as a decimal number. these are good for doing math.
* string- think of strings as a collection of characters. These can be letters, numbers or symbols. If you have numbers as a string type, you can't do math with them. When you create a string, use single or double quotes. That was why "Hello" was quoted in the first example.

Here are the functions we are going to use for types and changing types, We will use these functions by putting objects into the parenthesizes-
* `type()` this will tell us the type of an object
* `int()` this will make a number an integer
* `str()` this will make an object into a string
* `float()` this will make a number into a float

Now, in the python shell, we will use some functions to find out what type an object is and change an object's type. If you want to save that change, you will need to reassign the variable, that tells the computer that the name you chose for your variable is representing another object, in this case a different type of object.

```
>>> type("Hello world!")
<type 'str'>
>>> type(4)
<type 'int'>
>>> type(3.5)
<type 'float'>
>>> number = 7
>>> type(number)
<type 'int'>
>>> float(number)
7.0
>>> type(number)
<type 'int'>
>>> int(number)
7
>>> str(number)
'7'
>>> int(number)
7
>>> number = str(number)
>>> type(number)
<type 'str'>
>>>

```

###User input

Let's ask the user what they want.

```
>>> answer = raw_input("type your name")
>>> print "hello"
>>> print answer
```

But, what if we want to print this all on one line. For that, we will want to print our variable in the middle of a sentence.

```
>>> answer = raw_input("type your name")
>>> print "hello, %s!" %(answer)
```
We can add as may variables as we want!

```
>>> statement = "I like %s %s!" % ("fluffy", "bunnies")
>>> print(statement)
```
OK, now we are ready to make a file with a madlibs game!

(You can see a full example [here](https://github.com/LindsayYoung/Python-class-intro/blob/master/example_libs.py).)





# get user input and set variables
number = raw_input("give me a whole number ")
size = raw_input("give me a size ")
noun = raw_input("give me a noun, please ")
adjective = raw_input("give me an adverb ")

# create the test by passing variables into strings
beginning = "You won't believe why I am late to work today! I woke up at my usual time- %s o'clock." % (number)

middle = "That is when things got weird. I saw a very %s %s, of course this would make me late." % (size, noun)

end = "But, now that I have %s coding skills. I will never be late again." % (adjective)

# print the variables that have the formatted text
print(beginning)
print(middle)
print(end)

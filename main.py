# Hey guys, in this mega repl (for me) I will teach you everything you need to know about basic Python and where to go from there.
# If you want to learn Python you may be coming from three paths:
#   a) You don't know anything about programming (I don't know how you found this website and this tutorial, since this whole website is about coding)
#   b) You have some idea about programming. You may be knowing some other programming language and want to learn Python. Welcome, I hope you find Python interesting no matter what language you are coming from!
#   c) You know some Python already. Maybe you know a little bit and you want to know more. Maybe you already know Python and want to look for good tutorials to show other people or to strengthen old knowledge.
# I will try to make this easy for all three backgrounds. For those of you who know Python, we will be covering: the console, input and output, variables, if statements and conditions, loops, functions, and libraries.

# Let us start with our first program, called Hello World.
print("Hello World")
# What is Hello World and why do we write this as our first program? The early programmers used this for mainly two purposes, 1 was to ensure that their compiler/interpreter was working properly, and 2 was to learn how to do a print command, a command which is used a lot. Although there may be some programs which don't use print at all!
# Let us break this into 3 parts.
# a) print(): print does not mean printing a piece of paper, it means printing, or writing something to the console on its own (we do not have to type it in). The console is the dark window to the right (that says Python 3.8.2 followed by the date). We will be talking about why the brackets are there later. For now, just remember that the code will not work without the brackets.
# b) "": The quotation marks represent strings. We will be talking about strings in detail later. In short, any alphanumeric character or a special character is a string.
# c) Hello World: This is the string that we want to output. The string must be enclosed  in quotation marks. Even single quotes work for this purpose.
# Click Run. The first 

# Let us talk about whitespace. Any space, newline (When we press enter, we go to a new line) or tab (when we press tab, it goes through multiple spaces) is called whitespace. Python mostly ignores whitespace. So, if we type:
print("_____") # I will be using this as a separator to differentiate.
print ("Hello")
# The code will still run.
# However, you cannot put whitespace at the start of the line, except under special conditions. We will learn about this later.
# Obviously, you can have more than simple one-liners.
print("_____")
print("ABC")
print("DEF")
# You cannot write two print statements (statements are when we write print() or any other function. We will be learning functions later)
# Note how ABC and DEF are on two lines. If we want them to be on one line, we can use a single print statement- print("ABCDEF")
# Now, what if we wanted to only use one print statement to print ABC and DEF on two lines? Is it possible?
print("_____")
print("ABC\nDEF")
# Firstly, what is \n? \n is a newline character. When we type \n, it is like the equivalent of pressing Enter. You can separate your lines like this. So, if we incorporate the separator:
print("_____\nABC\nDEF") # It will have the same output.
# There is also \t which can be used to print tabs.
print("_____\nA\tB\tC")
# You can even combine two or more tabs or newlines.
print("_____\nA\t\tB\tC\n\nD")
# Exercise 1:
# 1) Create your own repl. (Go to repl.it and try to figure out how you can create a repl.)
# 2) Make a statement that prints a table-like structure with names, ages and hobby of 3 people. (Think how \t can be used for this purpose.)

# Let us talk about data types. 
# The data type which we have been using so far is called string. But, why do we call it a data type? Any form of text or number or anything is data. Data has several types, and we have used string so far. But are there other data types?
# Yes, there are other data types. Integer (a number), Float (a decimal number) and Boolean (a true or false value, we will be talking about this later). There are other data types, and we can even create our own!
# Other than strings, no other data type needs to be in double quotes.
print("_____")
print(5)
# We do not get an error. However, if we did print(abc) without quotes, we will get an error. Try finding out more about this error. We will be talking about the concepts involved in this error and errors in general later.
print("_____")
print(2.5)
# We can even print floats. Floats can be precise up to 15 digits. That means that if you had to, say store a number with more than 15 decimal places, it will automatically round it for you.
# Now what would be the point of numbers if we cannot store or do arithmetic?
print("_____")
print(5 + 5)
print(8 - 5)
print(5 * 3) # * means multiplying.
print(100 / 5) # / means dividing. Note how it shows 20.0 instead of 20.
print(2 ** 4) # ** means exponentiation. 2 ** 4 means 2 to the power four.
print(4 % 3) # % means modulo, or remainder. 4 % 3 will find the remainder of 4 / 3.
print(100 // 5) # Floor division or integer division. Instead of returning (outputting) a float value, it returns an integer value. Try finding out what happens if you floor divide two floats.

# We can even put brackets for order of importance.
print("_____")
print(5 * 2 + 4 / 3 - 1) # We get 10.3333 etc.
print(((5 * 2) + 4) / 3 - 1) # It will solve the innermost bracket (5 * 2) first. Try to figure out how the result comes as 3.6666 etc.

# Let us talk about comments. Comments are lines which are ignored by the interpreter. They start with a '#' sign and are used for notes. If you want to remove a line of code, but still want to keep it for future reference, you can "comment it out" (meaning put a # sign in front of it).
print("_____")
print("A") # You can event put a comment at the end of a line, but not start of the line. It will comment the whole line if you do so.
# print("B")
print("C") # Will print out A and C instead of A, B and C.
# In repl.it, if you do Ctrl + / it will comment the line your cursor is on. It will comment the whole line and not the place where your comment starts. Also, you can select multiple lines by dragging your mouse and doing Ctrl + /.

# Earlier I said that comments are ignored by the interpreter. What does interpreter mean? Interpreter is the program which is running, or executing (showing the output) of your code. It takes in the lines of code one by one and translates it into binary. It then gives it to the computer. The computer then runs the binary code. If a line starts with # it will ignore everything between # and the newline.
# Exercise 2:
# 1) Find out about compiler and how it is different from interpreter.
# 2) Find out about assembler.

# Let us talk about booleans and operators.
# Booleans are any true or false value.
print(True) # T and F have to be uppercase.
print(False) 

# What are operators? Operators are like mini-functions which are defined through symbols. You will understand more about this statement later.
# You already know 4 operators, +, -, *, /, //. These are called arithmetic operators. 
# There are other operators as well.
# a) Relational operator- It sees relation between two sides, LHS and RHS.
print("_____")
print(5 > 4) # This will print True.
print(4 < 6) 
print(4 <= 4) # This means 4 is less than or equal to 4. If LHS < RHS, it returns True, and if LHS = RHS, it will still output True.
print(4 >= 5) # Similar to <=, this is called greater than or equal to.
print(5 == 6) # This is equal to operator. If LHS = RHS, it will return True. You might think, why is it 5 == 6 and not 5 = 6? We will learn about this soon.
print(5 != 6) # Not equal to operator. If LHS is not equal to RHS, return True. Else, return false.

# b) Logical operator- There are 3 logical operators, and, or, not. First, let's learn some boolean logic.
# LHS and RHS returns True if LHS and RHS both equate to True, otherwise it will return False.
# LHS or RHS returns True if either LHS or RHS equates to True, otherwise it will return False.
# not STATEMENT will return True if STATEMENT is False and False if STATEMENT is True.
# I am adding brackets to easily differentiate between LHS and RHS. It can work fine even without brackets.

print("_____")
print((5 <= 6) and (5 <= 5)) # LHS = True and RHS = True, so return True.
print((5 >= 6) and (5 <= 5)) # LHS = False and RHS = True, so return False.
print((5 <= 6) and (5 == 8)) # LHS = True and RHS = False, so return False.
print((5 >= 6) and (5 == 8)) # LHS = False and RHS = False, so return False.

print("_____")
print((5 <= 6) or (5 <= 5)) # LHS = True and RHS = True, so return True.
print((5 >= 6) or (5 <= 5)) # LHS = False and RHS = True, so return True.
print((5 <= 6) or (5 == 8)) # LHS = True and RHS = False, so return True.
print((5 >= 6) or (5 == 8)) # LHS = False and RHS = False, so return False.

print("_____")
print(not (5 == 5)) # STATEMENT = True so return False.
print(not (6 == 5)) # STATEMENT = False so return True.

# Exercise 3:
# 1) Can you think of another way to write LHS != RHS?
# 2) Research and find if you can use logical operators like arithmetic operators and learn about their order precedence.

# There are more operators which we will learn about later.

# Now, let us talk about variables.
# What are variables? Variables are like a box or container that has an object, or value in it. When you call the variable, you will receive the value. It is like opening the box to see the object inside.
x = 5
print("_____")
print(x)
# Instead of printing "x" (a string) you print x (a variable). This variable, when printed, points to 5.
# Variables can have any data type. We can even combine variables and constants.
sep = "_____"
print(sep)
print(x + 5)

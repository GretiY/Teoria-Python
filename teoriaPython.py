from typing import Tuple


a = 5
x = "HELLO WORLD"
print(x)    
Quote = "I am a quote"
print(Quote)

if  a < 2:
    print("5 is less than 2")
else:    print("5 is not less than 2")

print("I am","25 years old") # This will cause an error because you cannot concatenate a string and an integer

nombre = "John"
print(f"Usuario: {nombre:>200}") # This will print the username right-aligned in a field of 200 characters
print(type(nombre)) # This will print the type of the variable 'nombre', which is <class 'str'>

# This is a comment
# This is another comment
# This is a third comment
# This is a fourth comment
# NO MULTILNE COMMENTS IN PYTHON

fruits = ["berry", "apple", "banana", "cherry"]
x, y, z, a = fruits
print(x) # This will print "berry"  
print(y) # This will print "apple"
print(z) # This will print "banana"
print(a) # This will print "cherry"

k = 10
j = 20
sum = k + j
print(k + j) # This will print 30
print(sum) # This will also print 30
print(k, j) # This will print 10 20

x = "awesome"   #Global variable can be used inside and outside of functions

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#String exercises
b = "viva la vida"
print([b]) # This will print ['viva la vida']
print(b[0]) # This will print 'v'
print(b[2:5])# This will print 'va '
print(b[:5]) # This will print 'viva '
print(b[5:]) # This will print 'la vida'
print(b[-5:]) # This will print 'vida'
print(b[-5:-2]) # This will print 'vid'
print(b.upper()) # This will print 'VIVA LA VIDA'
print(b.lower()) # This will print 'viva la vida'
print(b.split()) # This will print ['viva', 'la', 'vida']
print(b.replace("vida", "muerte")) # This will print 'viva la muerte'
print(f"{x}") # This will print 'awesome' because x is a global variable that was defined as "awesome"

txt = " We are the so-called \"Vikings\" from the north. "
txt2 = "We are the so-called 'Vikings' from the north."
txt3 = "We are the so-called \n\"Vikings\" from the north."
txt4 = "We are the so-called \t\"Vikings\" from the north."
txt5 = "We are the so-called \\\"Vikings\\\" from the north."
txt6 = " We are the so-called \f\"Vikings\" from the north. "
print(txt) # This will print ' We are the so-called "Vikings" from the north. '
print(txt2) # This will print "We are the so-called 'Vikings' from the north."
print(txt3) # This will print 'We are the so-called
print(txt4) # This will print 'We are the so-called     "Vikings" from the north.'
print(txt5) # This will print 'We are the so-called \"Vikings\"
print(txt6) # This will print ' We are the so-called \f"Vikings" from the north. '

x = [ "apple", "banana", "cherry"]
y = ["pineapple", "mango", "papaya"]
z = x
print(x is z) # This will print True because x and z refer to the same list
print(x is y) # This will print False because x and y refer to different lists
print(x == y) # This will print False because x and y have different contents
print(x == z) # This will print True because x and z have the same contents
print(x is not y) # This will print True because x and y refer to different lists
print(x is not z) # This will print False because x and z refer to the same

x = ["ford", "volvo", "bmw"]
y = ["citroen", "peugeot", "renault"]

print("volvo" in x) # This will print True because "volvo" is in the list x
print("citroen" in x) # This will print False because "citroen" is not in the list x
print("citroen" not in x) # This will print True because "citroen" is not in the list x
print("ford" not in y) # This will print True because "ford" is not in the list y

# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.




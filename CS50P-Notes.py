# I put my CS50P pythin notes over here 

print("Hello World")
# Prints "Hello World"

print(f"hello , {Var}")
# you can implemetn variables into strings like this 

input("type in a number")
# It would ask the user to type a number and it will sotre it

Var.strip()
# Cuts the extra space around the strings

Var.capitalize()
# turn "dan" into "Dan"
Var.title()
# Same thing but caps the first letter of each word

def function():
  #Creates a function, def for define
  #Has to be indented under 

def Hello(to):
  print("Hello,", to)
name = input("what's your name?")
Hello(name)



#symboles
> #greater
>= #greater or equal 
< #less then
<= #less then or equal
== #equal
!= # not equal



if ....:
  ....
elif ...:
  ...
#elif means else if



# you can use or to add another condition 
if x > y or x <y:
  print("X is not equal to y")
else:
  pritn("x is equal to y")




#while loops
i = 1
while i < 6:
  print(i)
  i += 1

#for loops
for i in range(3):
  print("meow")
range() #range function will give you numbers from the value that you assign to it but it won't go through the value (ex: range(3) = [0,1,2])


print("mewo\n" * 3, end="")
#does the smae thing as the loops above


white True:
  n = int(input("What's n?"))
  if n > 0:
    break
for _ in range(n):
  print("meow")

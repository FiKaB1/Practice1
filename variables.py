x = 5
y = "John"
print(x)
print(y)


age=11
name= "Aibek"
print(age)
print(name)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

vint=4
vstr="Ali"
print (vint)
print(vstr)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

x=int(9)
y="9"
z=float(3.14)
print(x)
print(y)
print(z)


x = 5
y = "John"
print(type(x))
print(type(y))

g="Ali"
#they are same
g='Ali'
print(g)


a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

#legal
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

'''illegal
2myvar = "John"
my-var = "John"
my var = "John"'''

x,y,z="Ali","Fatima","Nurshat"
print(x)
print(y)
print(z)


x=y=z= "Berik"
print(x)
print(y)
print(z)

names=["Ali","Fatima","Aisha"]
x,y,z=names
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python"
y = "is"
z = "awesome"
print(x + y + z)

a=5
b=10
print(a*b)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

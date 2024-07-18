<<<<<<< HEAD
x=10 #global variable
def show():
    x=20 #local variable 
    print(globals()['x'])
    return(x)
y=show()
print("value of inner x",y)
=======
x=10 #global variable
def show():
    x=20 #local variable 
    print(globals()['x'])
    return(x)
y=show()
print("value of inner x",y)
>>>>>>> 6d1c98303aa22a4372d0aec8643e57015c582b4e
print("value of outer x",x)
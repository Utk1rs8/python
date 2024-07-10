x=10 #global variable
def show():
    x=20 #local variable 
    print(globals()['x'])
    return(x)
y=show()
print("value of inner x",y)
print("value of outer x",x)
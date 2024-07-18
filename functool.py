import functools
mylist=[20,15,45,50,60]
def small(x,y):
    if x<y:
        return x
    else:
        return y
print(functools.reduce(small,mylist))
mylist1=[1,2,3,4,5]
mylist2=[6,7,8,9,10]
def add(x,y):
    return(x+y)
rawlist=list(map(add,mylist1,mylist2))
print(rawlist)
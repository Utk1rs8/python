n=int(input("enter the no. of rows u need"))
i=1
while i<=n:
    print((n-i)*(" ")," *"*i)
    i=i+1
i=i-2
while i>=1:    
    print((n-i)*(" ")," *"*i)
    i=i-1
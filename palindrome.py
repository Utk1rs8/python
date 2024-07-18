<<<<<<< HEAD
a=int(input("enter any name: "))
n,digit=a,0
while a>0:
    rev=a%10
    digit=digit*10+rev
    a=a//10
if digit==n:
    print("it is a palindrome no.")
else:
=======
a=int(input("enter any name: "))
n=a
digit=0
while a>0:
    rev=a%10
    digit=digit*10+rev
    a=a//10
if digit==n:
    print("it is a palindrome no.")
else:
>>>>>>> 6d1c98303aa22a4372d0aec8643e57015c582b4e
    print("it is not a palindrome no.")
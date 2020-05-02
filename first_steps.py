#fibonacci series --

#a, b = 0, 1
#while a<10:
#    #print(a, end='yousofine')
#    print(a)
#    a, b = b, a+b

#getting an input from the console
#x=int(input("Enter an integer, dipshit: "))

#while x != -99:
#    if x < 0:
#        print("This is a negative number, nu bueno")
#        x =0
#        x=int(input("Enter an integer, dipshit: "))
#    elif x==0:
#        print("Zero, just like you")
#        x=int(input("Enter an integer, dipshit: "))
#    elif x==1:
#        print("One, just like the number of your balls")
#        x=int(input("Enter an integer, dipshit: "))
#    else:
#        print("Try again to hit the lucky number")
#        x=int(input("Enter an integer, dipshit: "))
#

#for i in range(2,10,3):
#    print(i)

#iterating over indices

a = ["yo", "momma", "is", "a", "stupid", "bitch"]

#for i in range(len(a)):
#    print(i, a[i])

#for i,v in enumerate(a):
#    print(i, v)

def fib(n):
    a, b = 0, 1
    while a<n:
        print(a)
        a, b = b, a+b
    print()



fib(200)

f=fib

f(12)
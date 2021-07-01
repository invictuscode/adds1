#Function -->User defined // already defined
#pyttsx3
#Random
#maths
#1000+++ functions
print("imported...")
def adds(x, y): #-->x,y are called as arguments
    print(x, "is getting added with",y,"to give", x+y)
def subs(x,y):
    print(x, "is getting subtracted with",y,"to give", x-y)
    
    
#Find the next even number:
    
'''
example : 2-->4 1-->2
'''


def nexteven(x):
    if(x%2==0):
        print("The next even number is...",x+2)
    elif(x%2!=0):
        print("The next even number is...",x+1)
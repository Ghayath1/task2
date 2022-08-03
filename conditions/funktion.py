  
#(2,3)
def Num1(x,y):
    r=x,y
    return r
t=Num1(4,5)
print(t)

#(4)
def Num2(x=0,y=0):
    r=x,y
    return r
t=Num2()
print(t)


#(5)
def num3(x,y):
    r=x+y
    return r

Z=num3(2,4)
print(Z)
#(6)
l=(lambda x,y:x+y)
#(7)
l=(lambda x,y:x+y)(10,12)
#(8)
'''
Global variables
A global variable can be used anywhere
in the program as its scope is the entire program.
Local variables
Local variables can only be reached within their scope(like func() above)
'''

    




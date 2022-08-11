
class Calculator:
    def __init__(self):
        print('Welcome')
    def sum(self,x,y):
        return x+y
    def mul(self,x,y):
        return x*y

class SciCalc(Calculator):
  
    def power(self,x,y):
        return x**y


s=SciCalc()
print(s.sum(4,3))
print(s.mul(4,3))
print(s.power(4,3))

#(6)->Yes
#(9)-> yes
#(10)->I see that the result has not changed and the code has become better.

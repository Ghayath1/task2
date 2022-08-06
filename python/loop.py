'''
#(1)
x=0
while x<=10:
    print(x)
    x+=1

#(2)
for i in range(0,11):
    print(i)
#(3)
for i in range(0,11):
       if i==5:
           break
       print(i)
print("done")

#(4)
for i in range(0,11):
       if i==5:
           continue
       print(i)
#(5)
y=5
for x in range(1,6):
    print(y,'X',x,'=',y*x)

#(5)
for c in range(1,6):
   for p in range(1,6):
      h = c*p
      print (h,'\t',end=' ')
  
   print("__")

#(6)
for l in range(10,21):
    print(l)

#(7)
for l in range(10,101,3):
    print(l)
#(8)
for i in range(1,101):
    if i%2==0:
        print(i)
        '''
#(9)
j=2
while j<=101:
    if j%2==0:
     print(j)
     j=j+2
#(10)
for i in range(1,101):
    if i%2==0:
        print(i)

import random
list=["sang","kaghaz","gheichi"]
t=0
u=0
c=0
print('be bazi sang kaghaz gheichi khosh amadid --->   computer vs user')
while t<=5:
    print('user lotfan az bein sang kaghaz gheichi yeki ro entekhab kon:')
    user=input()
    computer=random.choice(list)
    print('entekhab computer:',computer)
    if user=='sang' and computer=='kaghaz':
     c+=1
     t+=1
   
    if user=='sang' and computer=='gheichi':
     u+=1
     t+=1
     
    if user=='kaghaz' and computer=='sang':
     u+=1
     t+=1
     
    if user=='kaghaz' and computer=='gheichi':
     c+=1
     t+=1
     
    if user=='gheichi' and computer=='sang':
     c+=1
     t+=1
    
    if user=='gheichi' and computer=='kaghaz':
     u+=1
     t+=1
    if t==5:
      break
if c>u:
    print ('computer is vin') 
elif c==u:
    print('masavi shodid')
elif u>c:
    print('user is vin')    

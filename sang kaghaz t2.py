import random

choos=["kaghaz","sang","gheichi"]
computer_user=0
conter_user =0
t=0
while True :
    print(" conter_user entekhabet ra vared kon:")
    a=input()
    computer_user=random.choice(choos)
    print("Computer:",computer_user)
    if conter_user== "kaghaz":
     if computer_user=="sang":
         conter_user+=1
         t+=1
         if(t==5):
          break
    if conter_user== "kaghaz":
     if computer_user=="gheichi":
        computer_user+=1
        t+=1
        if(t==5):
          break
    if conter_user== "sang":
     if computer_user=="gheichi":
        conter_user+=1
        t+=1
        if(t==5):
         break
    if conter_user== "sang":
     if computer_user=="kaghaz":
        computer_user+=1
        t+=1
        if(t==5):
         break
    if conter_user== "gheichi":
     if computer_user=="kaghaz":
         conter_user+=1
         t+=1
         if(t==5):
          break
    if conter_user== "gheichi":
     if computer_user=="sang":
          computer_user+=1
          t+=1
          if(t==5):
           break
    if conter_user== "sang":
     if computer_user=="kaghaz":
          computer_user+=1
          t+=1
          if(t==5):
           break
    if conter_user== "gheichi":
     if computer_user=="kaghaz":
          conter_user+=1
          t+=1
          if(t==5):
           break
    if conter_user== "gheichi":
     if computer_user=="sang":
          computer_user+=1
          t+=1
          if(t==5):
           break
    if conter_user== "kaghaz":
     if computer_user=="sang":
          conter_user+=1
          t+=1
          if(t==5):
           break
    if conter_user== "kaghaz":
     if computer_user=="gheichi":
          computer_user+=1
          t+=1
          if(t==5):
           break
    if conter_user== "sang":
     if computer_user=="gheichi":
           conter_user+=1
           t+=1
           if(t==5):
            break
if computer_user>conter_user:
 print('computer_user brande shod')          
else:
  print('conter_user brande shod') 

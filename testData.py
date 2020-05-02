from manageData import *
import time

sendStatus('old')

#print(isSubmit())

while(isSubmit()==False):
   time.sleep(1)
    
userName = getName()

print(userName)

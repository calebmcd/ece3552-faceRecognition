import requests
import os
import pickle

#url = 'http://pi.calebmcd.com:8000/'
url = 'http://localhost:1880'

def sendStatus(status):
    global url
    
    requests.post((url + '/status'), {'status':status})
    
def isSubmit():
    global url
    
    r = requests.get((url +'/isSubmit'))
    value = r.text
    
    if(value=='1'):
        return True
    else:
        return False
    
def sendName(userName):
    global url
    
    requests.post((url + '/name'), {'name':userName})
    
def getName():
    global url
    
    r = requests.get((url + '/getName'))
    userName = r.text
    
    return userName
    
def picButton():
    global url
    
    pressed = request.get((url + '/picTaken'))
    
    if(pressed):
        return True
    else:
        return False
import requests
import os
import pickle

#url = 'http://pi.calebmcd.com:8000/'
url = 'http://localhost:1880'

def sendStatus(status):
    global url
    
    requests.post((url + '/status'), {'status':status})
    
def sendName(userName):
    global url
    
    requests.post((url + '/name'), {'name':userName})
    
def getName():
    global url
    
    return userName = requests.get((url + '/getName'))
    
    
def picButton():
    global url
    
    pressed = request.get((url + '/picTaken'))
    
    if(pressed):
        return true
    else:
        return false
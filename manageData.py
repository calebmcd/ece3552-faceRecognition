import requests
import os
import json
from statistics import mean
import pandas as pd
import pickle

#url = 'http://pi.calebmcd.com:8000/'
url = 'http://50.89.231.68:8000'

def pullData():
    
    global userData
    global url
    
    userData = (requests.get(url + '/pulldata')).json()
    
    
def calculate():
    global userData
    bpmPath = 'bpmFile.pickle'
    
    pullData()
    
    print('Completing Calculations....')
    with open(bpmPath, 'rb') as lfi:
        totalBPM = pickle.load(lfi)
    
    with open('time', 'rb') as lt:
        timeDict = pickle.load(lt)
    
    #readUserData = open('userSettings', 'rb')
    #UserData = pd.read_pickle(
    
    age = userData['age']
    weight = userData['weight']
    
    time = (timeDict/60)
    avgHR = mean(totalBPM)
    
    calBurnedMale = ((age*0.2017)+(avgHR*0.6309)-(weight*0.09036)-55.0969)*(timeDict/4.184)
    fatBurnedMale = (calBurnedMale/3500)
    
    calBurnedFemale =((age*0.074)+(avgHR*0.4472)-(weight*0.05741)-20.4022)*(timeDict/4.184)
    fatBurnedFemale = (calBurnedFemale/3500)
    
    print("You burned ", round(calBurnedMale, 5), " calories and ", round(fatBurnedMale, 5), " pounds")
    print("You worked out for ",round(time,2)," minutes.")
    print("Your average heart rate was ", round(avgHR, 4))
    
    os.remove('time')
    os.remove(bpmPath)
    
    Stats = [round(time,2),round(calBurnedMale,4),round(fatBurnedMale,4),round(calBurnedFemale,4),round(fatBurnedFemale,4),round(avgHR,4)]
    return Stats
    

def send_data(statArray):
    
    global userData
    global url
    
    payload = {'time':statArray[0],'calMale':statArray[1],'fatMale':statArray[2],'calFemale':statArray[3],'fatFemale':statArray[4],'avgHR':statArray[5],'gender':userData['gender']}
     
    requests.post(url + '/data', json=payload)

def process():
    print('Calculating Data.....')
    data_to_send = calculate()
    print('Sending Data to Server.....')
    send_data(data_to_send)
    print('Data Sent!')

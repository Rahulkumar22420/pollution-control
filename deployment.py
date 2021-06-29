# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 18:06:32 2021

@author: ASUS
"""
import requests
import pandas as pd
import PySimpleGUI as pt
from tkinter import *
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np

df=pd.read_excel("water-_2 (1).xls")
df.sort_values(by='STATION CODE', ascending=True)
independent=df[['Code']]
dependent=df[['PH']]

x_train,x_test,y_train,y_test =train_test_split(independent,dependent,test_size=0.3)
rf=RandomForestRegressor()
model=rf.fit(np.array(x_train).reshape(-1,1),np.array(y_train).reshape(-1,1))
res=requests.get('https://ipinfo.io/')
print(res.text)
data=res.json()
print (data)
txt=data['region']
print(txt)
code=0
if txt=='Gujarat':
    code=1
if txt=='Maharastra':
    code=2
if txt=='Rajasthan':
    code=3
if txt=='Orissa' or txt=='Odisha':
    code=4
if txt=='Uttarakhand':
    code=5
if txt=='Pondicherry':
    code=6
if txt=='Haryana':
    code=7
if txt=='Kerala':
    code=8
if txt=='Andhra Pradesh':
    code=9
if txt=='Tripura':
    code=10
if txt=='Mizoram':
    code=11
if txt=='Himachal Pradesh': 
    code=12
if txt=='Goa':
    code=13
if txt=='Daman And Diu ':
    code=14
if txt=='Tamil Nadu':
    code=15
if txt=='Uttar Pradesh':
    code=16
if txt=='Punjab':
    code=17
if txt=='Meghalaya':
    code=18
if txt=='Karnataka':
    code=19
if txt=='Madhya Pradesh':
    code=20
if txt=='Delhi':
    code=21

print(code)
main_window=Tk()
main_window.geometry('1100x600')
Label(main_window , font=("Arial", 30),text="Tracking your live location" ,fg="white",bg="green").pack(pady=20,fill="x")
Label(main_window , font=("Arial", 25),text="Your Location" ,fg="white" ,bg="purple").pack(fill="x",pady=10)
Label(main_window , font=("Arial", 20),text=data['loc'] ,fg="white" ,bg="black").pack(fill="x")
Label(main_window , font=("Arial", 20),text=data['region'] ,fg="white" ,bg="black").pack(fill="x")
Label(main_window , font=("Arial", 20),text=data['timezone'] ,fg="white" ,bg="black").pack(fill="x")
Label(main_window , font=("Arial", 20),text=data['org'],fg="white", bg="black").pack(fill="x")
Label(main_window , font=("Arial", 20),text="Country: INDIA",fg="white" ,bg="black").pack(fill="x")
Label(main_window , font=("Arial", 30),text="Prediction" ,fg="white",bg="red").pack(pady=30,fill="x")
Result=np.array(rf.predict(np.array([[code]])))
print(Result)
if Result>7.0 and Result <7.5:
    Label(main_window,text="Slightly Polluted \n\n P.H. is inbetween 7.0 and 7.5",font=("Copperplate Gothic Bold", 25)).pack()
elif Result >7.5:
    Label(main_window ,text="Vigorously Polluted \n\n P.H. is greater than 7.5",font=("Copperplate Gothic Bold", 25)).pack()
else :
    Label(main_window, text ="Not Polluted \n\n P.H is nearly about 7",font=("Copperplate Gothic Bold", 25)).pack()
    



main_window.mainloop()






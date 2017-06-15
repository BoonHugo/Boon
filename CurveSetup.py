import datetime
import os
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np



def LireData():                 #recup data en str brut
    Brut = open("data.txt", "r")
    DataBrut = Brut.read()
    Brut.close()
    return DataBrut

def CreaList():                 #transfo Data en List
    TextBrut = LireData()
    while True:
        TextList = TextBrut.split("*")
        time.sleep(1)
        return TextList

def DatePropre():               #transfo str en datetime
    DateSale = CreaList()
    DateSale = DateSale[1:-1:2]
    DateSale = [datetime.datetime.strptime(x, "%d/%m/%y %H:%M") for x in DateSale]
    return DateSale

def TempPropre():
    TempSale = CreaList()
    TempSale = TempSale[0:-1:2]
    TempSale = [float(y) for y in TempSale]
    return TempSale

x = DatePropre()
y = TempPropre()
DeltaDate = (x[-1] - x[0])


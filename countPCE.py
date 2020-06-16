import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as cnst
from tkinter import *

root = Tk()

def forButton():
    info['text'] = ''
    proc = scal.get() / 100
    Pin = 100 * proc # Pin = [mW/cm2]
    try:
        result = notBadFunction(float(FF_entry.get()), float(Voc_entry.get()), float(Jsc_entry.get()))
        info['text'] += str(result / Pin)
    except:
        return

def notBadFunction(FF, Voc, Jsc):
    """
        :FF = [%]:
        :Voc = [V]:
        :Jsc = [mA/cm2]:
    """
    return (FF * Voc * Jsc)

#print(notBadFunction(60.812, 0.968, 11.194, 1))

FF_entry = Entry()
Voc_entry = Entry()
Jsc_entry = Entry()
info = Label(text='PCE = ')
one = Label(text='Введите FF : ')
two = Label(text='Введите Voc : ')
three = Label(text='Введите Jsc : ')
buttonCounter = Button(text='count', command=forButton)

scal = Scale(root,orient=HORIZONTAL,length=300,from_=0,to=100,tickinterval=10,resolution=1)

one.grid(row=0, column=0)
two.grid(row=1, column=0)
three.grid(row=2, column=0)
FF_entry.grid(row=0, column=1)
Voc_entry.grid(row=1, column=1)
Jsc_entry.grid(row=2, column=1)
scal.grid(row=3, column=0)
info.grid(row=4, column=0)
buttonCounter.grid(row=5, column=0)

root.mainloop()
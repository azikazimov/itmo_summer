import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as cnst
from tkinter import *

root = Tk()
root.title('PCE counter')

def forButton():
    info['text'] = 'PCE = '
    proc = procentSun.get() / 100
    Pin = 100 * proc # Pin = [mW/cm2]
    try:
        result = notBadFunction(float(FF_entry.get()), float(Voc_slider.get()), float(Jsc_slider.get()))
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
two = Label(text='бегунок Voc')
three = Label(text='бегунок Jsc')
four = Label(text='бегунок для настройки мощности солнца (%)')
buttonCounter = Button(text='count', command=forButton)

procentSun = Scale(root, orient=HORIZONTAL, length=600, from_=0, to=100, tickinterval=10, resolution=1)
#FF_slider = Scale(root,orient=HORIZONTAL,length=300,from_=0,to=100,tickinterval=0.01,resolution=0.01) # не нашел "желательное" минимальное значение FF для кремния
Voc_slider = Scale(root, orient=HORIZONTAL, length=600, from_=0.754, to=0.842, tickinterval=0.01, resolution=0.001)
Jsc_slider = Scale(root, orient=HORIZONTAL, length=600, from_=42.77, to=44.23, tickinterval=0.1
, resolution=0.01)

one.grid(row=0, column=0)
two.grid(row=4, column=1)
three.grid(row=5, column=1)
four.grid(row=3, column=1)
FF_entry.grid(row=0, column=1)
#Voc_entry.grid(row=1, column=1)
#Jsc_entry.grid(row=2, column=1)
procentSun.grid(row=3, column=0)
Voc_slider.grid(row=4, column=0)
Jsc_slider.grid(row=5, column=0)
info.grid(row=6, column=0)
buttonCounter.grid(row=7, column=0)

root.mainloop()
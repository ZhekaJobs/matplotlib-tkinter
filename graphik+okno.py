import tkinter as tk
from tkinter import filedialog
import os
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)

red = pd.read_csv("K:/pythoon/wind_dataset.csv")
#min
windmin=red['WIND'].min()
indmin=red['IND'].min()
rainmin=red['RAIN'].min()
ind1min=red['IND.1'].min()
tmaxmin=red['T.MAX'].min()
ind2min=red['IND.2'].min()
tminmin=red['T.MIN'].min()
tmingmin=red['T.MIN.G'].min()
#cредн
windmen=red['WIND'].mean()
indmen=red['IND'].mean()
rainmen=red['RAIN'].mean()
ind1men=red['IND.1'].mean()
tmaxmen=red['T.MAX'].mean()
ind2men=red['IND.2'].mean()
tminmen=red['T.MIN'].mean()
tmingmen=red['T.MIN.G'].mean()
#max
windmax=red['WIND'].max()
indmax=red['IND'].max()
rainmax=red['RAIN'].max()
ind1max=red['IND.1'].max()
tmaxmax=red['T.MAX'].max()
ind2max=red['IND.2'].max()
tminmax=red['T.MIN'].max()
tmingmax=red['T.MIN.G'].max()

date = [1961,1969,1978]
wind = [windmin,windmen,windmax]
rain = [rainmin,rainmen,rainmax]
ind1=[ind1min,ind1men,ind1max]
tmax=[tmaxmin,tmaxmen,tmaxmax]
ind2=[ind2min,ind2men,ind2max]
tmin=[tminmin,tminmen,tminmax]
tming=[tmingmin,tmingmen,tmingmax]

window = tk.Tk()
window.title('График wind_dataset.csv')
window.geometry('900x500')


def open_file():
    the_file = filedialog.askopenfilename(
      filetypes = [("All files", "*.*")]  
      )  
    os.startfile(os.path.abspath(the_file))

#создаем график
def plot():
    fig = Figure(figsize = (5, 5), 
                     dpi = 100)
    
    plot1 = fig.add_subplot(111)
    plot1.plot(wind,date)
    plot1.plot(rain,date)
    plot1.plot(ind1,date)
    plot1.plot(tmax,date)
    plot1.plot(ind2,date)
    plot1.plot(tmin,date)
    plot1.plot(tming,date)
    canvas = FigureCanvasTkAgg(fig, master = window)   
    canvas.draw()
    canvas.get_tk_widget().pack()
  
frame1=tk.Frame(borderwidth=8,relief=tk.RAISED)
frame2=tk.Frame(borderwidth=8,relief=tk.RAISED)
button1 = tk.Button(command = open_file, master=frame1,text='wind_dataset.csv', width =15 ,height=2 ,bg='#7f91a4',fg='white')
button2 = tk.Button(command = plot, master = frame2, text = 'график', width =15 ,height=2 ,bg='#7f91a4',fg='white')

frame1.place(x=0, y=120)
frame2.place(x=0, y=300)
button1.pack()
button2.pack()
window.mainloop()


 

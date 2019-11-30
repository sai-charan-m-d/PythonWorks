import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from math import pi
mpl.use("TkAgg")

plt.style.use('ggplot')
df =  pd.read_csv(r"E:\PythonStuff\pokemon\Pokemon.csv")
LARGE_FONT = ("Verdana",12)

df.columns = df.columns.str.upper().str.replace('_', '')
df.head()
df = df.set_index('NAME')
df.index = df.index.str.replace(".*(?=Mega)", "")
df=df.drop(['#'],axis=1)
df['TYPE 2'].fillna(df['TYPE 1'], inplace=True)
data=df
data.drop(["TYPE 1", "TYPE 2","TOTAL","GENERATION","LEGENDARY"], axis = 1, inplace = True)
Attributes =list(data)
AttNo = len(Attributes)
name1 = 'Ivysaur'
name2 = 'Venusaur'

values = data.loc[name1].tolist()
values += values [:1]

angles = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
angles += angles [:1]

values2 = data.loc[name2].tolist()
values2 += values2 [:1]

angles2 = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
angles2 += angles2 [:1]

class PokemonApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="PokeBall.ico")
        tk.Tk.wm_title(self,"Pokedex")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)

        self.frames = {}
        for F in (StartPage,PageOne,PageTwo,PageThree,PageFour):
            frame = F(container,self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0 , sticky = "nsew")
        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Start Page", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Scatter plot",
                            command=lambda:controller.show_frame(PageOne))
        button1.pack()
        button2 = ttk.Button(self, text="Box Plot",
                            command=lambda:controller.show_frame(PageTwo))
        button2.pack()
        button3 = ttk.Button(self, text="Spider Plot",
                            command=lambda:controller.show_frame(PageThree))
        button3.pack()
        button4 = ttk.Button(self, text="Violin Plot",
                            command=lambda:controller.show_frame(PageFour))
        button4.pack()
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Scatter plot attack vs defense", font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text="Back to home",
                            command=lambda:controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Next Page",
                            command=lambda:controller.show_frame(PageTwo))
        button2.pack()
        f = Figure(figsize=(5,5),dpi=100)
        ax = f.add_subplot(111,polar = False)
        ax.scatter(df.ATTACK,df.DEFENSE)
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side = tk.TOP, fill= tk.BOTH,expand = True)

        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side = tk.TOP, fill= tk.BOTH,expand = True)
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Box Plot", font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text="Back to home",
                            command=lambda:controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Next Page",
                            command=lambda:controller.show_frame(PageThree))
        button2.pack()
        
        f = Figure(figsize=(5,5),dpi=100)
        ax = f.add_subplot(111)
        ax.boxplot(x=df)
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side = tk.TOP, fill= tk.BOTH,expand = True)

        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side = tk.TOP, fill= tk.BOTH,expand = True)
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Spider Graph", font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text="Back to home",
                            command=lambda:controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Next Page",
                            command=lambda:controller.show_frame(PageFour))
        button2.pack()
        
        f = Figure(figsize=(5,5),dpi=100)
        ax = f.add_subplot(111,polar = True)
        ax.plot(angles,values)
        ax.fill(angles, values, 'blue', alpha=0.1)
        ax.plot(angles2,values2)
        ax.fill(angles2, values2, 'red', alpha=0.1)
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side = tk.TOP, fill= tk.BOTH,expand = True)

        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side = tk.TOP, fill= tk.BOTH,expand = True)

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Violin Plot", font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text="Back to home",
                            command=lambda:controller.show_frame(StartPage))
        button1.pack()
##        button2 = ttk.Button(self, text="next Page",
##                            command=lambda:controller.show_frame(PageThree))
##        button2.pack()  
        f = Figure(figsize=(5,5),dpi=100)
        ax = f.add_subplot(111)
        ax.violinplot(dataset=df)
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side = tk.TOP, fill= tk.BOTH,expand = True)

        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side = tk.TOP, fill= tk.BOTH,expand = True)

app = PokemonApp()
app.mainloop()

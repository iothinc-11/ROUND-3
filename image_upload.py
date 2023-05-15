from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import os, shutil
import PIL.Image
import webbrowser


class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Welcome to IoTHINC VITC")
        self.geometry('900x900')
        self.labelFrame = tk.LabelFrame(self,bg='#b038f5')
        #self.labelFrame.grid(column=0,row=1,padx= 20, pady= 20)
        fontStyle = tkFont.Font(family="Lucida Grande", size=12)
        self.btton()
        self.labelFrame.place(anchor="nw",x=50,y=50,width=800, height=550)
        self.configure(bg='black')
        self.label = tk.Label(self.labelFrame, text="",font=fontStyle,bg='#b038f5',fg='#FFFFFF')
        self.labelc = tk.Label(self.labelFrame, text="",font=fontStyle,bg='#b038f5',fg='#fFFFFF')
        self.label.grid(column =1,row = 2)
        self.labelc.grid(column =1,row = 100)
        pholder="\"Not all treasure is silver and gold, mate.\"\n   - Jack Sparrow"
        self.label.configure(text =pholder)
        

    def btton(self):
        self.button = tk.Button(self.labelFrame, text="Upload Image",height=2,width=15,command=self.fileDailog,bg="#d9a0fa",fg='#033500')
        self.button.grid(column=1,row=1)
        self.button.grid(padx=350,pady=70)
    def fileDailog(self):
        self.fileName = filedialog.askopenfilename(initialdir = "/", title="Select A File",filetype=(("png","*.png"),("jpeg","*.jpg")))
        #self.label = tk.Label(self.labelFrame, text="",bg='#0ff0fc',fg='#ff003f')
        #self.label.grid(column =1,row = 2)
        img = self.fileName
        image = PIL.Image.open(img, 'r')
        data = ''
        imgdata = iter(image.getdata())
        while (True):
                pixels = [value for value in imgdata.__next__()[:3] +
                                        imgdata.__next__()[:3] +
                                        imgdata.__next__()[:3]]

                binstr = ''

                for i in pixels[:8]:
                    if (i % 2 == 0):
                        binstr += '0'
                    else:
                        binstr += '1'

                data += chr(int(binstr, 2))
                if (pixels[-1] % 2 != 0):
                        #print(data)
                        self.label.configure(text = data)
                        self.label.bind("<Button-1>", lambda e: webbrowser.open_new_tab(data))
                        self.labelc.configure(text = "***PLEASE CLICK THE ABOVE LINK***")
                        #self.label.configure(text = x[0:10]+"\n"+x[10:20]+"\n"+x[20:30]+"\n"+x[30:40]+"\n"+x[40:50]+"\n")
                        break

if __name__ == '__main__':
    root = Root()
    root.mainloop()

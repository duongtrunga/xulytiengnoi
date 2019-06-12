#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import webbrowser
import speech_recognition as sr


root = Tk()
root.title('Tool search')
root.iconbitmap('mic.ico')


label1 = ttk.Label(root, text='Query:')
label1.grid(row=0, column=0)
entry1 = ttk.Entry(root, width=40)
entry1.grid(row=0, column=1, columnspan=4)

btn2 = StringVar()

def callback():
    
    if btn2.get() == 'google' and entry1.get() != '':
        webbrowser.open('http://google.com/search?q='+entry1.get())
        
    elif btn2.get() == 'ytb' and entry1.get() != '':
        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())

    else:
        pass

def get(event):

    if btn2.get() == 'google' and entry1.get() != '':
        webbrowser.open('http://google.com/search?q='+entry1.get())
        
    elif btn2.get() == 'ytb' and entry1.get() != '':
        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())

    else:
        pass

def buttonClick():



    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400

    with sr.Microphone() as source:

        try:

            audio = r.listen(source, timeout=5)
            message = str(r.recognize_google(audio))
            entry1.focus()
            entry1.delete(0, END)
            entry1.insert(0, message)

            if btn2.get() == 'google':
                webbrowser.open('http://google.com/search?q='+message)
        
            elif btn2.get() == 'ytb':
                webbrowser.open('https://www.youtube.com/results?search_query='+message)

            else:
                pass

        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio')

        except sr.RequestError as e:
            print('Could not request results from Google Speech Recognition Service')

        else:
            pass    

entry1.bind('<Return>', get)


MyButton1 = ttk.Radiobutton(root, text='Google', value='google', variable=btn2)
MyButton1.grid(row=1, column=1, sticky=W)

MyButton2 = ttk.Radiobutton(root, text='Ytb', value='ytb', variable=btn2)
MyButton2.grid(row=1, column=2, sticky=E)

MyButton3 = Button(root,text='voice', width=10, command=buttonClick, bd=0, activebackground='#c1bfbf', overrelief='groove', relief='sunken')
MyButton3.grid(row=0, column=5)

entry1.focus()
root.wm_attributes('-topmost', 1)
btn2.set('google')
root.mainloop()

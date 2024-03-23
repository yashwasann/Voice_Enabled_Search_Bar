from tkinter import *
from tkinter import ttk,messagebox
import webbrowser
import speech_recognition
from pygame import  mixer

mixer.init()

def search():
    if questionField.get()!='':
        if temp.get()=='google':
            webbrowser.open(f'https://www.google.com/search?q={questionField.get()}')
    else:
        messagebox.showerror('Error','There is nothing to be searched')

def voice():
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr=speech_recognition.Recognizer()
    with speech_recognition.Microphone()as m:
        try:
            sr.adjust_for_ambient_noise(m, duration=0.2)
            audio=sr.listen(m)
            message = sr.recognize_google(audio)
            mixer.music.load('music2.mp3')
            mixer.music.play()
            questionField.delete(0,END)
            questionField.insert(0,message)
            search()
        except:
            pass

root=Tk()

root.geometry('660x70+100+100')
root.title('Voice Enabled Search Bar')
root.iconbitmap('icon.ico')
root.config(bg='lightgrey')
root.resizable(0,0)

temp=StringVar()

style=ttk.Style()
style.theme_use('clam')

queryLabel=Label(root,text='Type/Click the Mic',font=('poppins',12,'bold'),bg='lightgrey')
queryLabel.grid(row=1,column=1)

questionField=Entry(root,width=45,font=('arial',14,'bold'),bd=4,relief=SUNKEN)
questionField.grid(padx=10,row=0,column=1)

micImage=PhotoImage(file='mic.png')
micButTon=Button(root,image=micImage,bg='lightgrey',bd=0,cursor='hand2',activebackground='lightgrey'
                 ,command=voice)
micButTon.grid(row=0,column=2)

searchImage=PhotoImage(file='search.png')

searchButton=Button(root,image=searchImage,bd=0,cursor='hand2',bg='lightgrey',activebackground='lightgrey'
                    ,command=search)
searchButton.grid(row=0,column=3,padx=5)

def enter_function(value):
    searchButton.invoke()

root.bind('<Return>',enter_function)

temp.set('google')

root.mainloop()
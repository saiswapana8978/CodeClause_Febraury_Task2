from tkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer
#colors
co1="#ffffff"
co2="#3C1DC6"
co3="#333333"
co4="#CFC7F8"

window=Tk()
window.title("")
window.geometry('352x225')
window.config(bg=co1)
window.resizable(width=FALSE,height=FALSE)

#events
def  play_music():
    running=listbox.get(ACTIVE)
    running_song['text']=running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def unpause_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def next_music():
    playing=running_song['text']
    index=songs.index(playing)
    new_index=index+1
    playing=songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0,END)
    show()
    listbox.select_set(new_index)
    running_song['text']=playing

def prev_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index-1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)
    show()
    listbox.select_set(new_index)
    running_song['text']=playing

#frames
leftframe=Frame(window,width=150,height=150,bg=co1)
leftframe.grid(row=0,column=0,padx=1,pady=1)
rightframe=Frame(window,width=250,height=150,bg=co3)
rightframe.grid(row=0,column=1,padx=0)
downframe=Frame(window,width=400,height=100,bg=co4)
downframe.grid(row=1,column=0,columnspan=3,padx=0,pady=1)

#rightframe
listbox=Listbox(rightframe,selectmode=SINGLE,font=("Arial 9 bold"),width=22,bg=co3,fg=co1)
listbox.grid(row=0,column=0)

w=Scrollbar(rightframe)
w.grid(row=0,column=1)

listbox.config(yscrollcommand=w.set)
w.config(command=listbox.yview)
#images
img_1=Image.open('icons/icon.png')
img_1=img_1.resize((150,150))
img_1=ImageTk.PhotoImage(img_1)

img_2=Image.open('icons/back.png')
img_2=img_2.resize((30,30))
img_2=ImageTk.PhotoImage(img_2)
back_button=Button(downframe,height=40,width=40,font=("Ivy 10"),bg=co4,padx=10,image=img_2,command=prev_music)
back_button.place(x=20,y=25)

img_3=Image.open('icons/next.png')
img_3=img_3.resize((30,30))
img_3=ImageTk.PhotoImage(img_3)
next_button=Button(downframe,height=40,width=40,font=("Ivy 10"),bg=co4,padx=10,image=img_3,command=next_music)
next_button.place(x=70,y=25)

img_4=Image.open('icons/pause.png')
img_4=img_4.resize((30,30))
img_4=ImageTk.PhotoImage(img_4)
pause_button=Button(downframe,height=40,width=40,font=("Ivy 10"),bg=co4,padx=10,image=img_4,
                    command=pause_music)
pause_button.place(x=120,y=25)

img_5=Image.open('icons/play.png')
img_5=img_5.resize((30,30))
img_5=ImageTk.PhotoImage(img_5)
play_button=Button(downframe,height=40,width=40,font=("Ivy 10"),bg=co4,padx=10,image=img_5,
                   command=play_music)
play_button.place(x=170,y=25)

img_6=Image.open('icons/stop.png')
img_6=img_6.resize((30,30))
img_6=ImageTk.PhotoImage(img_6)
stop_button=Button(downframe,height=40,width=40,font=("Ivy 10"),bg=co4,padx=10,image=img_6,
                   command=stop_music)
stop_button.place(x=220,y=25)

img_7=Image.open('icons/unpause.png')
img_7=img_7.resize((30,30))
img_7=ImageTk.PhotoImage(img_7)
unpause_button=Button(downframe,height=40,width=40,font=("Ivy 10"),bg=co4,padx=10,image=img_7,
                      command=unpause_music)
unpause_button.place(x=270,y=25)

app_image=Label(leftframe,height=130,image=img_1,bg=co1)
app_image.place(x=10,y=15)

line=Label(leftframe,width=200,height=1,padx=10,bg=co3)
line.place(x=0,y=1)

line=Label(leftframe,width=200,height=1,padx=10,bg=co1)
line.place(x=0,y=3)

running_song=Label(downframe,text="Choose a song",width=44,font=("Ivy 10"),height=1,bg=co1,fg=co3,anchor=NW)
running_song.place(x=0,y=1)

os.chdir(r'C:\Users\Hello\PycharmProjects\MusicPlayer\pythonProject1\music')
songs=os.listdir()
def show():
    for i in songs:
            listbox.insert(END, i)

show()
mixer.init()
music_state=StringVar()
music_state.set("Choose one!")
window.mainloop()
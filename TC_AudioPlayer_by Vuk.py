### WINDOWS 10 ###
 
##########################
###  m4a,wav,webm,mp3  ###
##########################
 
import os
 
try: from moviepy.editor import AudioFileClip as afc
except: os.system('pip install moviepy')
try: import vlc
except: os.system('pip install python-vlc')
try: import cv2
except: os.system('pip install opencv-python')
 
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from tkinter import *
from tkinter.ttk import *
import threading
import datetime
import time
 
root=Tk()
### FRAME_1 ###
widget_frame1 = Frame(root)
widget_frame1.grid(row=0,column=0,padx=10,pady=10)
 
btn_choose = Button(widget_frame1,text='Choose file')
btn_choose.grid(row=0,column=0,padx=10,pady=10)
 
btnChooseFolder = Button(widget_frame1,text='Choose folder')
btnChooseFolder.grid(row=0,column=1,padx=10,pady=10)
 
lbl_time = Label(widget_frame1,text='0:00:00')
lbl_time.grid(row=0,column=2,padx=10,pady=10)
 
lbl_time_length = Label(widget_frame1,text='0:00:00')
lbl_time_length.grid(row=0,column=4,padx=10,pady=10)
 
ScaleVar = DoubleVar()
ScaleVar.set(0)
scale = Scale(widget_frame1,from_=0,to=0,orient=HORIZONTAL,length=360,
              variable=ScaleVar)
scale.grid(row=0,column=3,padx=10,pady=10)
 
### FRAME_2 ###
from tkinter import *
widget_frame2 = Frame(root)
widget_frame2.grid(row=2,column=0,padx=10,pady=10)
 
 
lblCurrentMusic = Label(widget_frame2,text='None')
lblCurrentMusic.grid(row=2,column=0,padx=10,pady=10)
def frame2Style():
    widget_frame2['bg'] = 'gray13'
    widget_frame2.update()
    
    lblCurrentMusic['font'] = ('Calibri',20,'bold')
    lblCurrentMusic['bg'] = 'deepskyblue'
    lblCurrentMusic['fg'] = 'white'
    lblCurrentMusic.update()
frame2Style() 
 
from tkinter.ttk import *
### FRAME_3 ###
widget_frame3 = Frame(root)
widget_frame3.grid(row=3,column=0,padx=10,pady=10)
 
btn_play = Button(widget_frame3,text='Play')
btn_play.grid(row=1,column=0,padx=10,pady=10)
 
btn_pause = Button(widget_frame3,text='Pause')
btn_pause.grid(row=1,column=1,padx=10,pady=10)
 
btn_stop = Button(widget_frame3,text='Stop')
btn_stop.grid(row=1,column=2,padx=10,pady=10)
 
lb_frame = Frame(root)
lb_frame.grid(row=4,column=0,padx=10,pady=10)
 
sbar = Scrollbar(lb_frame)
sbar.pack(side = RIGHT,fill = Y)
 
from tkinter import *
lb_items = Listbox(lb_frame,font=('Calibri',20,'bold'),width=55, height=20,
                   yscrollcommand=sbar.set)
lb_items.pack(fill = BOTH, expand=True)
lb_items.config(yscrollcommand = sbar.set)
sbar.config(command = lb_items.yview)
def StyleLbFrame():
    lb_items['bg'] = 'gray23'
    lb_items['fg'] = 'white'
    lb_items.update()
StyleLbFrame()
 
from tkinter.ttk import *
def style():
    FONT = ('Arial',15,'bold')
    BG = 'deepskyblue'
    FG = 'white'
    WIDTH = 25
 
    try: lbl_time_length['font'] = FONT
    except: print(end='')
    #lbl_time['bg'] = BG
    #lbl_time['fg'] = FG
    try: lbl_time_length['width'] = 7
    except: print(end='')
    try: lbl_time['font'] = FONT
    except: print(end='')
    #lbl_time['bg'] = BG
    #lbl_time['fg'] = FG
    try: lbl_time['width'] = 7
    except: print(end='')
    try: btn_choose['font'] = FONT
    except: print(end='')
    try: btn_choose['bg'] = BG
    except: print(end='')
    try: btn_choose['fg'] = FG
    except: print(end='')
    try: btn_choose['width'] = WIDTH - 10
    except: print(end='')
    try: btnChooseFolder['font'] = FONT
    except: print(end='')
    try: btnChooseFolder['bg'] = BG
    except: print(end='')
    try: btnChooseFolder['fg'] = FG
    except: print(end='')
    try: btnChooseFolder['width'] = WIDTH - 10
    except: print(end='')
    try: btn_stop['font'] = FONT
    except: print(end='')
    try: btn_stop['bg'] = BG
    except: print(end='')
    try: btn_stop['fg'] = FG
    except: print(end='')
    try: btn_stop['width'] = WIDTH + (int(WIDTH * 0.5))
    except: print(end='')   
    try: btn_pause['font'] = FONT
    except: print(end='')
    try: btn_pause['bg'] = BG
    except: print(end='')
    try: btn_pause['fg'] = FG
    except: print(end='')
    try: btn_pause['width'] = WIDTH + (int(WIDTH * 0.5))
    except: print(end='')
    try:btn_play['font'] = FONT
    except: print(end='')  
    try: btn_play['bg'] = BG
    except: print(end='') 
    try: btn_play['fg'] = FG
    except: print(end='')   
    try: btn_play['width'] = WIDTH + (int(WIDTH * 0.5))
    except: print(end='')
style()
 
def state():
    btn_play['state'] = 'disabled'
    btn_play.update()
    btn_pause['state'] = 'disabled'
    btn_pause.update()
    btn_stop['state'] = 'disabled'
    btn_stop.update()
    scale['state'] = 'disabled'
    scale.update()
state()
 
lst_music = []
 
global folder
folder = ''
 
def choose_folder():
    lst_music.clear()
    lb_items.delete(0,END)
    lb_items.update()
    PathFolder = str(askdirectory())
    if not PathFolder == '':
        ListFiles = os.listdir(PathFolder)
        for item in ListFiles:
            AbsPath = str(PathFolder) + '/' + str(item)
            lst_music.append(AbsPath)
            lb_items.insert(len(lst_music),os.path.basename(lst_music[-1]))
            lb_items.update()
btnChooseFolder['command'] = lambda: choose_folder()
 
global file
file = ''
 
def choose_file():
    file = str(askopenfilename())
    if not file == '':
        if file.endswith('.m4a') or\
           file.endswith('.wav') or\
           file.endswith('.webm') or\
           file.endswith('.mp3'):
            btn_play['state'] = 'normal'
            btn_play.update()
            global AUDIO_PATH
            AUDIO_PATH = file
            BASE_NAME = os.path.basename(file)
            FileSize = str(round(os.path.getsize(file) / pow(1024, 2), 2)) + 'MB'
            lst_music.append(file)
            lb_items.insert(len(lst_music),os.path.basename(lst_music[-1]))
            lb_items.update()
            scale['from_'] = 0
            scale.update()
            global AUDIO_PATH_DURATION
            AUDIO_PATH_DURATION = int(afc(file).duration)
            scale['to'] = AUDIO_PATH_DURATION#int(afc(AUDIO_PATH).duration)
            scale.update()
            LENGTH = str(datetime.timedelta(seconds=AUDIO_PATH_DURATION))
            lbl_time_length['text'] = LENGTH
            lbl_time_length.update()
        
            root.title('Audio Player - ' + str(BASE_NAME) + ' - ' + str(FileSize))
            root.update()
                
btn_choose['command'] = lambda: choose_file()
 
def play_audio():
    try:
        if AUDIO_PATH.endswith('.m4a') or\
           AUDIO_PATH.endswith('.wav') or\
           AUDIO_PATH.endswith('.webm') or\
           AUDIO_PATH.endswith('.mp3'):
            btn_choose['state'] = 'disabled'
            btn_choose.update()
            global Instance
            Instance = vlc.Instance()
            global audio_player
            audio_player = Instance.media_player_new()
            audio_player.audio_set_volume(70)
            global Media
            Media = Instance.media_new(AUDIO_PATH)
            Media.get_mrl()
            audio_player.set_media(Media)
            audio_player.play()
            scale['from_'] = 0
            scale.update()
            scale['to'] = AUDIO_PATH_DURATION#int(afc(AUDIO_PATH).duration)
            scale.update()
            btn_play['state'] = 'disabled'
            btn_play.update()
            btn_pause['state'] = 'normal'
            btn_pause.update()
            btn_stop['state'] = 'normal'
            btn_stop.update()
            scale['state'] = 'normal'
            scale.update()
 
            def CurrentMusicInfo():
                NumberAudio = str(int(lb_items.curselection()[0])+1)
                TotalAudio = str(len(lst_music))
                GetAudioPath = str(lst_music[int(lb_items.curselection()[0])])
                BaseNamePath = os.path.basename(GetAudioPath)
                FinalStringAudio = NumberAudio + '/' + str(TotalAudio) + ' -> ' + str(BaseNamePath)
 
                lblCurrentMusic['text'] = str(FinalStringAudio)
                lblCurrentMusic.update()
            CurrentMusicInfo()
            
            while True:
                root.update()
                time.sleep(1)
                value = int(audio_player.get_time() / 1000)
                
                convert = str(datetime.timedelta(seconds=value))
                if value == AUDIO_PATH_DURATION-1:#int(afc(AUDIO_PATH).duration)-1:
                    stop_audio()
                    try:
                        lbl_time['text'] = str(datetime.timedelta(seconds=0))
                        lbl_time.update()
                    except:
                        print(end='')
                    break
 
                try:
                    ScaleVar.set(value)
                    ScaleVar.update()
                except:
                    print(end='')
                
                try:
                    lbl_time['text'] = convert
                    lbl_time.update()
                except:
                    print(end='')
    except:
        print(end='')
         
def thread_play_audio():
    try:
        obj = threading.Thread(target=lambda: play_audio())
        obj.start()
    except:
        print(end='')
 
def stop_audio():
    audio_player.stop()
    btn_choose['state'] = 'normal'
    btn_choose.update()
    btn_play['state'] = 'normal'
    btn_play.update()
    btn_pause['state'] = 'disabled'
    btn_pause.update()
    btn_stop['state'] = 'disabled'
    btn_stop.update()
    scale.set(0)
    scale.update()
    scale['state'] = 'disabled'
    scale.update()
 
def clickEvent(event):
    try:
        stop_audio()
    except:
        print(end='')
    text = lb_items.get(lb_items.curselection())
    #print(lb_items.curselection()[0],text)
    global AUDIO_PATH
    AUDIO_PATH = lst_music[int(lb_items.curselection()[0])]
    LENGTH = str(datetime.timedelta(seconds=AUDIO_PATH_DURATION))#int(afc(AUDIO_PATH).duration)))
    lbl_time_length['text'] = LENGTH
    lbl_time_length.update()
    BASE_NAME = os.path.basename(AUDIO_PATH)
    FileSize = str(round(os.path.getsize(AUDIO_PATH) / pow(1024, 2), 2)) + 'MB'
    root.title('Audio Player - ' + str(BASE_NAME) + ' - ' + str(FileSize))
    root.update()
    try:
        thread_play_audio()
    except:
        print(end='')
lb_items.bind('<Double-Button-1>', clickEvent)
 
def clickEvent_ChoosePath(event):
    #PATH = lst_music[int(lb_items.curselection()[0])]
    #print('AUDIO_PATH',PATH)
    
    #text = lb_items.get(lb_items.curselection())
    #print(lb_items.curselection()[0],text)
    global AUDIO_PATH
    AUDIO_PATH = lst_music[int(lb_items.curselection()[0])]
    global AUDIO_PATH_DURATION
    AUDIO_PATH_DURATION = int(afc(AUDIO_PATH).duration)
    LENGTH = str(datetime.timedelta(seconds=AUDIO_PATH_DURATION))#int(afc(AUDIO_PATH).duration)))
    lbl_time_length['text'] = LENGTH
    lbl_time_length.update()
    BASE_NAME = os.path.basename(AUDIO_PATH)
    FileSize = str(round(os.path.getsize(AUDIO_PATH) / pow(1024, 2), 2)) + 'MB'
 
    try:
        NumberAudio = str(int(lb_items.curselection()[0])+1)
        TotalAudio = str(len(lst_music))
        FinalStringAudio = NumberAudio + '/' + str(TotalAudio)
 
        root.title('Audio Player - ' + str(FinalStringAudio) + ' <-> ' + str(BASE_NAME) + ' - ' + str(FileSize))
        root.update()
    except:
        root.title('Audio Player - ' + str(BASE_NAME) + ' - ' + str(FileSize))
        root.update()
 
lb_items.bind('<<ListboxSelect>>', clickEvent_ChoosePath)
 
def scale_value(ev=None):
    try:
        value = int(scale.get())
        convert = str(datetime.timedelta(seconds=value))
 
        if value == AUDIO_PATH_DURATION:#int(afc(AUDIO_PATH).duration):
            #audio_player.stop()
            stop_audio()
            btn_play['state'] = 'normal'
            btn_play.update()
            btn_pause['state'] = 'disabled'
            btn_pause.update()
            btn_stop['state'] = 'disabled'
            btn_stop.update()
            scale['state'] = 'disabled'
            scale.update()
 
        audio_player.set_time(value * 1000)
    except:
        print(end='')
scale['command'] = scale_value
 
def thread_stop_audio():
    obj = threading.Thread(target=lambda: stop_audio())
    obj.start()
 
def commands():
    btn_play['command'] = lambda: thread_play_audio()
    btn_pause['command'] = lambda: audio_player.pause()
    btn_stop['command'] = lambda: thread_stop_audio()
commands()
 
if __name__ == '__main__':
    root.title('TC_Audio Player_by Vuk')
    root.configure(bg='gray13')
    root.resizable(False,False)
    root.mainloop()
 

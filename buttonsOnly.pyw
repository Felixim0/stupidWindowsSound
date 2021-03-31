from tkinter import *
import subprocess

master = Tk()
master.title("VolumeMaster 2.0")

CREATE_NO_WINDOW = 0x08000000
# Create all IntVars, set to 0

def executeCommand(command):

    #command = "cd C:/Users/Felix/Music & " + command
    print(command)
    subprocess.call(command, creationflags=CREATE_NO_WINDOW)
    # use above for final to hide command window, use below for testing
    subprocess.call(command)

r = 0
ok_volumes = [0,30,50,80,100]
for ok_volume in ok_volumes:
    Button(master, text = f'{ok_volume}%', command = lambda ok_volume=ok_volume: executeCommand(f'./changeVolume.exe {ok_volume}'), width = 20,font = ("Times", 30)).grid(row=r,column=1,columnspan=10)
    r = r + 1

mainloop()

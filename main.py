from tkinter import *
import subprocess

master = Tk()
master.title("Select Groups")

rows=10
columns=11

boxes = []
boxVars = []
CREATE_NO_WINDOW = 0x08000000
# Create all IntVars, set to 0

for i in range(rows):
    boxVars.append([])
    for j in range(columns):
        boxVars[i].append(IntVar())
        boxVars[i][j].set(0)

def executeCommand(command):

    #command = "cd C:/Users/Felix/Music & " + command
    print(command)
    subprocess.call(command, creationflags=CREATE_NO_WINDOW)
    # use above for final to hide command window, use below for testing
    subprocess.call(command)

def checkRow(i):
    global boxVars, boxes




def getSelected(boxVars):
    selected = {}
    temp = []
    for i in range(len(boxVars)):
        for j in range(len(boxVars[i])):
            if str(boxVars[i][j].get()) == "1":
                boxVars[i][j].set("0")
                temp.append([i,j])

    if temp != []:
        print (temp)
        x , y = temp[0][0], temp[0][1]
        vol = y+x *10
        executeCommand(f'./changeVolume.exe {vol}')

ok_volumes = [0,30,50,80,100]
added_vols = []
count = 0
for x in range(rows):
    boxes.append([])
    for y in range(columns):
        coly = y * 2
        count = y+x *10
        boxes[x].append(Checkbutton(master, variable = boxVars[x][y], command = lambda x = x: checkRow(x)))
        
        if count in ok_volumes:
            if count not in added_vols:
                added_vols.append(count)
                if count == 0:
                    boxes[x][y].grid(row=x, column=coly,columnspan=2)                
                    Label(master, text= f'{count} %',font = ("Times", 30)).grid(row=x,column=coly+1,columnspan=1000)
                else:
                    boxes[x][y].grid(row=x, column=coly)                
                    Label(master, text= f'{count} %',font = ("Times", 30)).grid(row=x,column=coly+1)


b = Button(master, text = "Set Volume", command =lambda boxVars = boxVars: getSelected(boxVars), width = 10)
b.grid(row = 12, column = 0,columnspan=1000)
mainloop()

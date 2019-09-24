import PySimpleGUI as sg
import sys, csv
from datetime import datetime

rightnow = datetime.now()
nowtime = rightnow.time()
nowHour = nowtime.hour
nowMinute = nowtime.minute
nowDate= rightnow.date()
nowWeekday = nowDate.weekday()
#get the minute
print(nowHour)
print(nowMinute)
print(nowWeekday)

def feedback():
    layout = [ #creates prompt where user can imput the specific URL, time and day of week.
        [sg.Text ('Please enter your satisfaction rate of the plan from 1-10, in terms of productivity and interms of the date and time')],
        [sg.Text('satisfaction', size=(20,1)), sg.InputText()],
        [sg.Text('productivity', size=(15,2)), sg.InputText()],
        [sg.Text('date and time', size=(15,3)), sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('simple entry window').Layout(layout)#connects the window to layout and creates it

    event, values = window.Read()#saves the entered values into an array.

    window.Close()

    print(event, values)# displays values saved to the console

    with open('reviewlogs.csv', mode= 'a') as ENTRIEZ: #opens the CSV
        WR = csv. writer(ENTRIEZ, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL) #edits positioning

        WR.writerow(values)#connects the array and puts it into the file

    ENTRIEZ.close()#closes the file

def MainPlan():#establsihes a function for view1

    layout = [ #creates prompt where user can imput the specific URL, time and day of week.
        [sg.Text ('Please enter your URLs, time,')],
        [sg. Text('enter the day of the week for this plan EX:monday=0 through sunday=6', size=(10,5)), sg.InputText()],
        [sg.Text('URL1', size=(5,1)), sg.InputText()],
        [sg.Text ('Enter the time, it should be 24 hour (16:40)')],
        [sg.Text('start time1', size=(15,2)), sg.InputText()],
        [sg.Text('end time1', size=(20,2)), sg.InputText()],
        [sg.Text('URL2', size=(5,1)), sg.InputText()],
        [sg.Text('start time2', size=(15,2)), sg.InputText()],
        [sg.Text('end time2', size=(20,2)), sg.InputText()],
        [sg.Text('URL3', size=(5,1)), sg.InputText()],
        [sg.Text('start time3', size=(15,2)), sg.InputText()],
        [sg.Text('end time3', size=(20,2)), sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('simple data entry window').Layout(layout)#connects the window to layout and creates it

    event, values = window.Read()#saves the entered values into an array.

    window.Close()

    print(event, values)# displays values saved to the console

    with open('datalogs.csv', mode= 'a') as ENTRIEZ: #opens the CSV
        WR = csv. writer(ENTRIEZ, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL) #edits positioning

        WR.writerow(values)#connects the array and puts it into the file

    ENTRIEZ.close()#closes the file


def Signin():
    layout = [ #creates prompt where user can imput the specific URL, time and day of week.
        [sg.Text ('Please enter your name')],
        [sg.Text('name', size=(5,1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ]
    window = sg.Window('simple data entry window').Layout(layout)#connects the window to layout and creates it

    event, values = window.Read()#saves the entered values into an array.

    window.Close()
    if values[0]== "Ben":
        MainPlan()

    if values[0]== "Logan":
        feedback()
Signin()

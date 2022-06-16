import tkinter as tkinter
import tkinter.font as tkFont

mainWindow = tkinter.Tk()
mainWindow.title("MEETING ROOM BOOKING")

font_Style = tkFont.Font(family="Calibri", size=12, weight="bold")

label_display = tkinter.Label(mainWindow, text="", height=2, width=22)
label_display.grid(row=0, column=0, columnspan=4)

# Buttons for the first row: days

button_time = tkinter.Button(mainWindow, text="Time", width=7, font=font_Style)
button_time.grid(row=1, column=0)

button_Sunday = tkinter.Button(mainWindow, text="Sunday", width=9, font=font_Style)
button_Sunday.grid(row=1, column=1)

button_Monday = tkinter.Button(mainWindow, text="Monday", width=9, font=font_Style)
button_Monday.grid(row=1, column=2)

button_Tuesday = tkinter.Button(mainWindow, text="Tuesday", width=9, font=font_Style)
button_Tuesday.grid(row=1, column=3)

button_Wednesday = tkinter.Button(mainWindow, text="Wednesday", width=9, font=font_Style)
button_Wednesday.grid(row=1, column=4)

#buttons for all the periods + break + lunch + form time

button_Period1 = tkinter.Button(mainWindow, text="Period 1", width=7, height=3, font=font_Style)
button_Period1.grid(row=2, column=0)

button_Period2 = tkinter.Button(mainWindow, text="Period 2", width=7, height=3, font=font_Style)
button_Period2.grid(row=3, column=0)

button_Break = tkinter.Button(mainWindow, text="Break", width=7, height=3, font=font_Style)
button_Break.grid(row=4, column=0)

button_Period3 = tkinter.Button(mainWindow, text="Period 3", width=7, height=3, font=font_Style)
button_Period3.grid(row=5, column=0)

button_Period4 = tkinter.Button(mainWindow, text="Period 4", width=7, height=3, font=font_Style)
button_Period4.grid(row=6, column=0)

button_lunch = tkinter.Button(mainWindow, text="Lunch", width=7, height=3, font=font_Style)
button_lunch.grid(row=7, column=0)

button_Form = tkinter.Button(mainWindow, text="Form", width=7, height=3, font=font_Style)
button_Form.grid(row=8, column=0)

button_Period5 = tkinter.Button(mainWindow, text="Period 5", width=7, height=3, font=font_Style)
button_Period5.grid(row=9, column=0)

button_Period6 = tkinter.Button(mainWindow, text="Period 6", width=7, height=3, font=font_Style)
button_Period6.grid(row=10, column=0)

#buttons for all Period 1 bookings

button_P1Sun = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P1Sun.grid(row=2, column=1)

button_P1Mon = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P1Mon.grid(row=2, column=2)

button_P1Tue = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P1Tue.grid(row=2, column=3)

button_P1Wed = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P1Wed.grid(row=2, column=4)

#buttons for all Period 2 bookings

button_P2Sun = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P2Sun.grid(row=3, column=1)

button_P2Mon = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P2Mon.grid(row=3, column=2)

button_P2Tue = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P2Tue.grid(row=3, column=3)

button_P2Wed = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P2Wed.grid(row=3, column=4)

#buttons for all Break bookings

button_BrSun = tkinter.Button(mainWindow, text="", width=9, height=3)
button_BrSun.grid(row=4, column=1)

button_BrMon = tkinter.Button(mainWindow, text="", width=9, height=3)
button_BrMon.grid(row=4, column=2)

button_BrTue = tkinter.Button(mainWindow, text="", width=9, height=3)
button_BrTue.grid(row=4, column=3)

button_BrWed = tkinter.Button(mainWindow, text="", width=9, height=3)
button_BrWed.grid(row=4, column=4)

#buttons for all Period 3 bookings

button_P3Sun = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P3Sun.grid(row=5, column=1)

button_P3Mon = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P3Mon.grid(row=5, column=2)

button_P3Tue = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P3Tue.grid(row=5, column=3)

button_P3Wed = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P3Wed.grid(row=5, column=4)

#buttons for all Period 4 bookings

button_P4Sun = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P4Sun.grid(row=6, column=1)

button_P4Mon = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P4Mon.grid(row=6, column=2)

button_P4Tue = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P4Tue.grid(row=6, column=3)

button_P4Wed = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P4Wed.grid(row=6, column=4)

#buttons for all Lunch bookings

button_LunchSun = tkinter.Button(mainWindow, text="", width=9, height=3)
button_LunchSun.grid(row=7, column=1)

button_LunchMon = tkinter.Button(mainWindow, text="", width=9, height=3)
button_LunchMon.grid(row=7, column=2)

button_LunchTue = tkinter.Button(mainWindow, text="", width=9, height=3)
button_LunchTue.grid(row=7, column=3)

button_LunchWed = tkinter.Button(mainWindow, text="", width=9, height=3)
button_LunchWed.grid(row=7, column=4)

#buttons for all Form bookings

button_FSun = tkinter.Button(mainWindow, text="", width=9, height=3)
button_FSun.grid(row=8, column=1)

button_FMon = tkinter.Button(mainWindow, text="", width=9, height=3)
button_FMon.grid(row=8, column=2)

button_FTue = tkinter.Button(mainWindow, text="", width=9, height=3)
button_FTue.grid(row=8, column=3)

button_FWed = tkinter.Button(mainWindow, text="", width=9, height=3)
button_FWed.grid(row=8, column=4)

#buttons for all Period 5 bookings

button_P5Sun = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P5Sun.grid(row=9, column=1)

button_P5Mon = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P5Mon.grid(row=9, column=2)

button_P5Tue = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P5Tue.grid(row=9, column=3)

button_P5Wed = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P5Wed.grid(row=9, column=4)

#buttons for all Period 6 bookings

button_P5Sun = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P5Sun.grid(row=10, column=1)

button_P5Mon = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P5Mon.grid(row=10, column=2)

button_P5Tue = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P5Tue.grid(row=10, column=3)

button_P5Wed = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P5Wed.grid(row=10, column=4)

#buttons for Thursday

button_TimeThu = tkinter.Button(mainWindow, text="Time", width=7)
button_TimeThu.grid(row=1, column=8, padx=(30,0))

class MeetingRoom():
  def __init__(self):
      self.root = tkinter.Tk()
      button_TimeThu = tkinter.Label(self.root, font=font_Style)
      button_Thursday = tkinter.Label(self.root, text="Hello World", font=font_Style)
      button_TimeThu.grid(row=0, column=0, padx=(100,10))
      button_Thursday.grid(row=1, column=0, padx=(10,100))

      app = MeetingRoom()
      app.root.mainloop()

button_P1Thu = tkinter.Button(mainWindow, text="Period 1", width=7, height=3, font=font_Style)
button_P1Thu.grid(row=2, column=8, padx=(30,0))

button_P2Thu = tkinter.Button(mainWindow, text="Period 2", width=7, height=3, font=font_Style)
button_P2Thu.grid(row=3, column=8, padx=(30,0))

button_P3Thu = tkinter.Button(mainWindow, text="Period 3", width=7, height=3, font=font_Style)
button_P3Thu.grid(row=4, column=8, padx=(30,0))

button_BrThu = tkinter.Button(mainWindow, text="Break", width=7, height=3, font=font_Style)
button_BrThu.grid(row=5, column=8, padx=(30,0))

button_P4Thu = tkinter.Button(mainWindow, text="Period 4", width=7, height=3, font=font_Style)
button_P4Thu.grid(row=6, column=8, padx=(30,0))

button_P5Thu = tkinter.Button(mainWindow, text="Period 5", width=7, height=3, font=font_Style)
button_P5Thu.grid(row=7, column=8, padx=(30,0))

button_Thursday = tkinter.Button(mainWindow, text="Thursday", width=9, font=font_Style)
button_Thursday.grid(row=1, column=9)

def ThuP1Window():
   ThuP1 = tkinter.Toplevel(mainWindow)
   ThuP1.geometry("750x250")
   ThuP1.title("Booking for Period 1 Thursday")
   #Create a Label in New window
   tkinter.Label(ThuP1, text="Teacher:").grid(row=0, column=1)

   def on_Click():
       tkinter.labelTeacher["text"] = f"Teacher: {tkinter.Teacher.get()}"

   Create = tkinter.Button(ThuP1Window, text="Create Booking", command=on_Click).grid(row=4, column=1)

   def Delete_Booking():
       # Teacher.delete(0,10)
       tkinter.labelTeacher["text"] = f"Teacher: {tkinter.Teacher.delete(0, 10)}"

   Delete = tkinter.Button(ThuP1Window, text="Delete Booking", command=Delete_Booking).grid(row=4, column=0)


tkinter.Button(mainWindow, text="Book", width=9, height=3, command=ThuP1Window).grid(row=2, column=9)

button_P2Thu = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P2Thu.grid(row=3, column=9)

button_P3Thu = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P3Thu.grid(row=4, column=9)

button_BreakThu = tkinter.Button(mainWindow, text="", width=9, height=3)
button_BreakThu.grid(row=5, column=9)

button_P4Thu = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P4Thu.grid(row=6, column=9)

button_P5Thu = tkinter.Button(mainWindow, text="", width=9, height=3)
button_P5Thu.grid(row=7, column=9)

mainWindow.mainloop()

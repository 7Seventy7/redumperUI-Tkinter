from textwrap import fill
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import font

root = tk.Tk()
#root.iconbitmap("redumper.ico")
root.title("  redumper")
root.geometry
import glob, os, shutil, subprocess



# Row 0: "Output Title" row
myLabel_OutputTitle = Label(root, text="Output File / Folder Name:", justify=LEFT)
myLabel_OutputTitle.grid(sticky=W, column=0, columnspan=2, row=0, padx=8, pady=(7, 1))
# Telling the myButton_OutputTitle button what to do once clicked
OutputTitle = Entry(root, width=35)
OutputTitle.grid(sticky=W, row=0, column=2, columnspan=4, padx=5.5, pady=(7, 1))
OutputTitle.insert(0, "(enter game title here)")
def myClick_OutputTitle():
    myClickLabel_OutputTitle = Label(root, text=OutputTitle.get())
    myClickLabel_OutputTitle.grid(padx=8, pady=(7, 1))
# "Select Directory" button
def getFolderPath():
    folder_selected = filedialog.askdirectory(initialdir=folderPath.get())
    folderPath.set(folder_selected)

folderPath = StringVar()
folderPath.set(os.getcwd())
btnFind = ttk.Button(root, text="Select Directory", command=getFolderPath)
btnFind.grid(row=0, column=7, padx=8, pady=(7,1))



# Row 1: "Drive Letter" row -- DISABLING FOR NOW
#drives = [ chr(x) + ":" for x in range(65,91) if os.path.exists(chr(x) + ":") ]
#myLabel_DriveLetter = Label(root, text="Drive Letter:")
#myLabel_DriveLetter.grid(sticky=W, row=1, column=0, padx=8, pady=0)
#clicked_DriveLetter = StringVar()
#clicked_DriveLetter.set("Auto")
#myDrop_DriveLetter = OptionMenu(root, clicked_DriveLetter, drives)
#myDrop_DriveLetter.grid(sticky=W, row=1, column=2, padx=0, pady=0)



# Row 2: "Drive Speed" row
myLabel_DriveSpeed = Label(root, text="Drive Speed:")
myLabel_DriveSpeed.grid(sticky=W, row=2, column=0, padx=8, pady=0)
clicked_DriveSpeed = StringVar()
clicked_DriveSpeed.set("Max")
# SupportedDriveSpeeds list to be replaced with auto-detected drive speeds.
SupportedDriveSpeeds = ["Max","72","64","48","32","16","8","4","2"]
myDrop_DriveSpeed = OptionMenu(root, clicked_DriveSpeed, *SupportedDriveSpeeds)
myDrop_DriveSpeed.grid(sticky=W, row=2, column=2, padx=3, pady=0)
# Define the selected speed value
SelectedDriveSpeed = StringVar()
def change_mydrop(*args):
    SelectedDriveSpeed.set(clicked_DriveSpeed.get())
if clicked_DriveSpeed.get() == "Max":
     SelectedDriveSpeed.set("72")
else:
    SelectedDriveSpeed.set(clicked_DriveSpeed)
clicked_DriveSpeed.trace("w", change_mydrop)



# Row 3: "Allow Non-Preservation-Grade Drives" row
myLabel_AllowDrives = Label(root, text="Allow Unsupported Drives:")
myLabel_AllowDrives.grid(sticky=W, row=3, column=0, columnspan=2, padx=8, pady=0)
checkbox_AllowDrives = StringVar()
myCheckbox_AllowDrives = Checkbutton(root, text="", variable=checkbox_AllowDrives, onvalue="--unsupported", offvalue="")
myCheckbox_AllowDrives.grid(sticky=W, row=3, column=2, padx=0, pady=0)



# Row 4: Advanced Settings frame start
frame = LabelFrame(root, text="Advanced Settings", padx=8, pady=8)
frame.grid(padx=10, column=0, columnspan=20, pady=10)



# Row 5: "Leave these settings to default if you are unsure of useage."
myLabel_AdvSetLeaveDefault = Label(frame, text="Leave these settings kept at their defaults if you are unsure of useage.")
myLabel_AdvSetLeaveDefault.grid(sticky=W, row=5, column=0, columnspan=19, padx=10, pady=(3, 10))



# Row 6: "Mode" row
myLabel_Mode = Label(frame, text="Mode:")
myLabel_Mode.grid(sticky=W, row=6, column=0, padx=10, pady=1)
clicked_Mode = StringVar()
clicked_Mode.set("cd")
myDrop_Mode = OptionMenu(frame, clicked_Mode, "cd", "dump", "protection", "refine", "split", "info")
myDrop_Mode.grid(sticky=W, row=6, column=1, padx=3, pady=1)



# Row 7: "Retry Amount" row
myLabel_Retries = Label(frame, text="Retry Amount:")
myLabel_Retries.grid(sticky=W, row=7, column=0, padx=10, pady=1)
myEntry_Retries = Entry(frame, width=20, fg="#000000", borderwidth=1)
myEntry_Retries.grid(sticky=W, row=7, column=1, columnspan=19, padx=(5,0), pady=1)
myEntry_Retries.insert(0, "50")



# Row 8: "Stop LBA (for fake TOC)" [TEXT BOX]
#myLabel_StopLBA = Label(frame, text="Stop LBA (for fake TOC):")
#myLabel_StopLBA.grid(sticky=W, row=8, column=0, padx=10, pady=1)
#myEntry_StopLBA = Entry(frame, width=20, fg="#000000", borderwidth=1)
#myEntry_StopLBA.grid(sticky=W, row=8, column=1, columnspan=19, padx=(5,0), pady=1)
#myEntry_StopLBA.insert(0, "Enter sector range.")



# Row 9: "Skip LBA Range" [TEXT BOX]
#myLabel90 = Label(frame, text="Skip LBA Range (for fake TOC):")
#myLabel90.grid(sticky=W, row=9, column=0, padx=10, pady=1)
#myEntry91 = Entry(frame, width=20, fg="#000000", borderwidth=1)
#myEntry91.grid(sticky=W, row=9, column=1, columnspan=19, padx=(5,0), pady=1)
#myEntry91.insert(0, "Enter sector range.")



# Row 10: "Zero-out erroneous sectors" [CHECKBOX]
myLabel_ZeroOut = Label(frame, text="Zero-out erroneous sectors:")
myLabel_ZeroOut.grid(sticky=W, row=10, column=0, padx=10, pady=1)
checkbox_ZeroOut = StringVar()
myCheckbox_ZeroOut = Checkbutton(frame, text="", variable=checkbox_ZeroOut, onvalue="--zero-error-sectors", offvalue="")
myCheckbox_ZeroOut.grid(sticky=W, row=10, column=1, padx=(0), pady=1)



# Row 11: "Skip Lead-in:" [CHECKBOX]
myLabel_SkipLeadIn = Label(frame, text="Skip Lead-In sectors:")
myLabel_SkipLeadIn.grid(sticky=W, row=11, column=0, padx=10, pady=1)
checkbox_SkipLeadIn = StringVar()
myCheckbox_SkipLeadIn = Checkbutton(frame, text="", variable=checkbox_SkipLeadIn, onvalue="--skip-leadin", offvalue="")
myCheckbox_SkipLeadIn.grid(sticky=W, row=11, column=1, padx=0, pady=1)



# Row 12: "Skip Size (for ringed discs)": [TEXT BOX]
#myLabel_SkipSize = Label(frame, text="Skip Size (for ringed discs):")
#myLabel_SkipSize.grid(sticky=W, row=12, column=0, padx=10, pady=1)
#myEntry_SkipSize = Entry(frame, width=20, fg="#000000", borderwidth=1)
#myEntry_SkipSize.grid(sticky=W, row=12, column=1, columnspan=19, padx=(5,0), pady=1)
#myEntry_SkipSize.insert(0, "Enter value.")



# Row 13: "Ring Size (for ringed discs)": [TEXT BOX]
#myLabel_RingSize = Label(frame, text="Ring Size (for ringed discs):")
#myLabel_RingSize.grid(sticky=W, row=13, column=0, padx=10, pady=1)
#myEntry_RingSize = Entry(frame, width=20, fg="#000000", borderwidth=1)
#myEntry_RingSize.grid(sticky=W, row=13, column=1, columnspan=19, padx=(5,0), pady=1)
#myEntry_RingSize.insert(0, "Enter value.")



# Row 14: "Parameters:" [TEXT ENTRY BOX AUTO-FILLED WITH COMMAND LINE PARAMETERS AS DECIDED BY GUI SELECTIONS] -- DISABLING FOR NOW
#myLabel_Parameters = Label(frame, text="Parameters:")
#myLabel_Parameters.grid(sticky=W, row=14, column=0, padx=10)
#myEntry_Parameters = Entry(frame, width=35, fg="#000000", borderwidth=1)
#myEntry_Parameters.grid(row=14, column=1, columnspan=19)
#myEntry_Parameters.insert(0, "myButton_StartDumping values here")



# Row 15: "Start Dumping"
def myClick_StartDumping():
    myButton_StartDumping = Label(root, command=subprocess.run([
        'redumper.exe',
        clicked_Mode.get(),
        "--image-path="+folderPath.get()+"/"+OutputTitle.get(),
        checkbox_AllowDrives.get(),
        "--speed="+SelectedDriveSpeed.get(),
        "--retries="+myEntry_Retries.get(),
        checkbox_ZeroOut.get(),
        checkbox_SkipLeadIn.get()]))
    myButton_StartDumping.grid()
myButton_StartDumping = Button(root, text="Start Dumping", command=myClick_StartDumping, fg="#0057B7", bd=3)
myButton_StartDumping.grid(row=15, column=2, padx=(14, 0), pady=(10, 18))



root.mainloop()
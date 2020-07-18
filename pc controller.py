import os
import webbrowser
input=input(str("What would you like to open:"))
if "sublime" in input:
    sublime_dir="C:\Program Files\Sublime Text 3\sublime_text.exe"
    os.startfile(os.path.join(sublime_dir))
if "zoom" in input:
    zoom_dir="C:\\Users\\KHALID\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
    os.startfile(os.path.join(zoom_dir))
if "shareit" in input:
    shareit_dir="C:\\Program Files\\SHAREit Technologies\\SHAREit\\SHAREit.exe"
    os.startfile(os.path.join(shareit_dir))
if "google" in input:
    webbrowser.open("www.google.com")
if "gmail" in input:
    webbrowser.open("www.gmail.com")
if "youtube" in input:
    webbrowser.open("www.youtube.com")
if "my site" in input:
    webbrowser.open("www.dpl.unaux.com")
if "facebook" in input:
    webbrowser.open("www.facebook.com")
if "insta"in input:
    webbrowser.open("www.instagram.com")
if "whatsapp web" in input:
    webbrowser.open("www.whatsappweb.com")
if "notepad++" in input:
    notepad_dir="C:\\Program Files\\Notepad++\\notepad++.exe"
    os.startfile(os.path.join(notepad_dir))
if "cmd" in input:
    cmd_dir="C:\\Windows\\System32\\cmd.exe"
    os.startfile(os.path.join(cmd_dir))
if "python file" in input:
    pythonfile_dir="D:\\Python file\\python"
    os.startfile(os.path.join(pythonfile_dir))
if "khalid" in input:
    khalid_dir="D:\\KHALID"
    os.startfile(os.path.join(khalid_dir))
if "irfan" in input:
    irfan_dir="D:\\Irfan"
    os.startfile(os.path.join(irfan_dir))
if "show me irfan pics" in input:
    pics_dir="D:\\Irfan\\Irfan pics\\My fav pics\\Irfan Pics"
    os.startfile(os.path.join(pics_dir))
if "downloads" in input:
    downloads_dir="C:\\Users\\KHALID\\Downloads"
    os.startfile(os.path.join(downloads_dir))
if "softwares" in input:
    software_dir="D:\\Softwares"
    os.startfile(os.path.join(software_dir))
if "disk c" in input:
    diskc_dir="C:\\"
    os.startfile(os.path.join(diskc_dir))
if "disk d" in input:
    diskd_dir="D:\\"
    os.startfile(os.path.join(diskd_dir))


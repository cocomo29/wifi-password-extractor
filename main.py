from subprocess import check_output, CalledProcessError
from tkinter import *
from turtle import onclick

data = check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
names = []

for i in data:
    if "All User Profile" in i:
        names.append(i.split(":")[1][1:-1])
        
result = {}

try:
    for i in names:
        password = check_output(["netsh", "wlan", "show", "profile", i, "key=clear"]).decode("utf-8").split("\n")
        for j in password:
            if "Key Content" in j:
                result[i] = j.split(":")[1][1:-1]
                break
            else:
                result[i] = ""
except CalledProcessError:
    print("[!] Couldn't Retrieve Profiles. Are you sure this is a Windows System?")
    exit(0)

win = Tk()
win.title("Wifi Passwords")
win.geometry("500x600")
win.configure(background="black")

Label(win, text="Wifi Passwords", bg="#121212", fg="white", font="hack 24 bold").pack(pady=25)

btn = Button(win, text="Show Passwords", bg="#121212", fg="white", font="hack 10", command=lambda: show_passwords(),padx=5,pady=5,borderwidth=1)
btn.pack(pady=15)
btn.bind("<Enter>", lambda event: btn.config(bg="black", fg="white"))
btn.bind("<Leave>", lambda event: btn.config(bg="#121212", fg="white"))

#border radius on canvas
frame = Canvas(win, bg="#121212", bd=10, highlightbackground="#121212", highlightthickness=10)
frame.pack(pady=25)

scrollbar = Scrollbar(frame)
if len(result) > 10:
    scrollbar.pack(side=RIGHT, fill=Y)
    frame.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=frame.yview)



def show_passwords():
    for i in result:
        Label(frame, text=f"{i} : {result[i]}", bg="#121212", fg="white", font="hack 10").pack(pady=10,padx=10,anchor='w')

win.mainloop()
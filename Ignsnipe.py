import webbrowser
from random import choice
from string import ascii_uppercase
import requests
import tkinter as tk
import string



root = tk.Tk()
root.title("Minecraft Ign Picker")

def RandomNameGen(): #pyinstaller.exe --onefile IgnSnipe.py
    RandomNames = (''.join(choice(ascii_uppercase + string.digits + "_") for i in range(3)))
    ploadss = {'name': 2}
    rs = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{RandomNames}', params=ploadss)
    try:
        rdat = rs.json()
        print(rdat["name"] + " is Taken")
        write2 = open("namestaken.txt", "a")
        write2.write("\n" + rdat["name"] + " is Taken")
    except:
        print(f"{RandomNames} is Not Taken")
        write =  open("names.txt", "a")
        write.write(f"\n{RandomNames} is Not Taken")

def CheckAvaiblity():
    try:
        name = input("What Is The Ign To See Avaiblity? ")
        r = requests.get(f"https://account.mojang.com/available/minecraft/{name}")
        rdat = r.json()
        print(rdat["name"] + " is Taken His uuid is " + rdat["id"])
    except:
        print(f"{name} is Not Taken Here is More Info On it On Namemc")
        webbrowser.open(f"https://namemc.com/search?q={name}")


window = tk.Canvas(height=700, width=700)
window.pack()

bg = tk.PhotoImage(file="C:/Users/User/Desktop/app/creep.png")

mylabel = tk.Label(root, image=bg)
mylabel.place(x=0,y=0, relwidth=1, relheight=1)

Button1= tk.Button(root,text="Pick Random IGN", padx=10,pady=5,fg="purple",bg="#e71f82", command=RandomNameGen)
Button1.pack()

Button12= tk.Button(root,text="Check Avaiblity", padx=10,pady=5,fg="purple",bg="#e71f82", command=CheckAvaiblity)
Button12.pack()




window.mainloop()

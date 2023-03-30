import tkinter as tk
import os
import subprocess

path = "./eCW/Upgrde 10.1.2022/web/Plugin 4.6.1164.msi"

window = tk.Tk()
window.title("Software Installation")
title = tk.Label(text="Select the software you want to install:")
title.pack()

app1 = tk.Checkbutton(text="App1")
app1.pack()

app2 = tk.Checkbutton(text="App2")
app2.pack()

app3 = tk.Checkbutton(text="App3")
app3.pack()


def install_apps():
    if app1.get() == 1:
        subprocess.call(os.path.join(path, "app1.exe"))
    if app2.get() == 1:
        subprocess.call(os.path.join(path, "app2.exe"))
    if app3.get() == 1:
        subprocess.call(os.path.join(path, "app3.exe"))


install_button = tk.Button(text="Install", command=install_apps)
install_button.pack()

quit_button = tk.Button(text="Quit", command=window.quit)
quit_button.pack()

window.mainloop()

import tkinter as tk
import os
import changeDir
import listElems

currentCwd = os.getcwd()


def makePath(listOfDirs):
    return '\\'.join(listOfDirs)


def enter(event):
    command = text.get("1.0", tk.END).splitlines()[-1]  # Take the last command
    command = list(map(str, command.split()))
    global currentCwd
    if command[0] == 'cd':
        res = changeDir.ChangeDirectory(command, currentCwd).doTheThing()
        if len(command) == 1:
            text.insert(tk.END, '\n' + res)  # Will writes documentation
        elif res[:5] == 'Error':
            text.insert(tk.END, '\n' + res, 'err')
        else:
            currentCwd = makePath(changeDir.ChangeDirectory(command, currentCwd).doTheThing())
    elif command[0] == 'ls':
        text.insert(tk.END, '\n')
        text.insert(tk.END, listElems.Ls(command[1:]).showList())
    text.insert(tk.END, '\n')
    text.insert(tk.END, currentCwd, 'cwd')


root = tk.Tk()
text = tk.Text(bg='black', fg='white', insertbackground='#24E016')
text.pack()
text.bind('<Return>', enter)

text.tag_config('cwd', foreground='#24E016')
text.tag_config('err', foreground='#FF1818')

text.insert(tk.END, os.getcwd(), 'cwd')
text.insert(tk.END, '\n', 'cwd')
root.mainloop()

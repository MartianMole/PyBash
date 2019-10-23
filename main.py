import tkinter as tk
import os
import changeDir
import listElems
import concatenation


currentPath = os.getcwd()


def makePath(listOfDirs):
    return '\\'.join(listOfDirs)


def enter(event):
    command = text.get("1.0", tk.END).splitlines()[-1]  # Take the last command
    command = list(map(str, command.split()))
    global currentPath
    if not command:
        pass
    elif command[0] == 'cd':
        res = changeDir.ChangeDirectory(command, currentPath).doTheThing()
        if len(command) == 1 or command[1] == '-h':
            text.insert(tk.END, '\n' + changeDir.__doc__)
        elif res[:5] == 'Error':
            text.insert(tk.END, '\n' + res, 'err')
        else:
            currentPath = makePath(changeDir.ChangeDirectory(command, currentPath).doTheThing())
    elif command[0] == 'ls':
        res = listElems.Ls(command[1:], currentPath).showList()
        if len(command) == 2 and command[1] == '-h':
            text.insert(tk.END, '\n' + listElems.__doc__)
        elif res[:5] == 'Error':
            text.insert(tk.END, '\n' + res, 'err')
        else:
            text.insert(tk.END, '\n')
            if command[-1][0] == '.':
                text.insert(tk.END, listElems.Ls(command[1:], currentPath, requestPath=command[-1]).showList())
            else:
                text.insert(tk.END, listElems.Ls(command[1:], currentPath).showList())
    elif command[0] == 'cat':
        if len(command) == 2 and command[1] == '-h':
            text.insert(tk.END, '\n' + concatenation.__doc__)
        else:
            if len(command) >= 2:
                concatenation.Concatenation(command[1:-1], command[-1], text, tk, currentPath).writeContent()
    elif command[0] == 'exit' and len(command) == 1:
        root.quit()
    elif command[0] == 'clear' and len(command) == 1:
        text.delete('1.0', tk.END)
    else:
        text.insert(tk.END, '\nError: Wrong request', 'err')
    text.insert(tk.END, '\n')
    text.insert(tk.END, currentPath, 'cwd')


root = tk.Tk()
root.resizable(0, 0)
root.title('PyBash')
text = tk.Text(bg='black', fg='white', insertbackground='#24E016')
text.pack()
text.bind('<Return>', enter)

text.tag_config('cwd', foreground='#24E016')
text.tag_config('err', foreground='#FF1818')

text.insert(tk.END, os.getcwd(), 'cwd')
text.insert(tk.END, '\n', 'cwd')
root.mainloop()

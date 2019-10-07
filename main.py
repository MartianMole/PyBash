import tkinter as tk
import os


def enter(event):
    t = text.get("1.0", tk.END).splitlines()[-1]
    t = list(map(str, t.split()))
    if t[0] == 'cd':
        print(1)
    text.insert(tk.END, '\n')
    text.insert(tk.END, os.getcwd(), 'cwd')
    print(t)


root = tk.Tk()
text = tk.Text(bg='black', fg='white', insertbackground='green')
text.pack()
text.bind('<Return>', enter)
text.tag_config('cwd', foreground='#24E016')
text.insert(tk.END, os.getcwd(), 'cwd')
text.insert(tk.END, '\n')
root.mainloop()

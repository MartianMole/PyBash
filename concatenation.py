from os import path

__doc__ = '''
================ls================
Command showing list of directories and files

==> Usage:
ls [keys]

==> Keys:
-h help
-a shows hidden files and folders
-l shows pretty list with numbers, sizes and types(folder or file)

==> Examples: 
ls -a:
    folder file
ls -l:
    .hidden folder file
ls -la:
ultra mega cool list:
    1) .hidden_________file____4
    2) folder__________folder__0
    3) file____________file____4096
ls -h - manual for noobs:
    *recursion*
================ls================
'''


class Concatenation:
    def __init__(self, keys, file, text, tk):
        self.keys = keys
        self.file = file
        self.text = text
        self.tk = tk

    def makeKeysList(self):
        keys = self.keys
        result = []
        for i in keys:
            if i[0] == '-':
                for j in i[1:]:
                    result.append(j)
        return result

    def writeContent(self):
        keys = Concatenation.makeKeysList(self)
        text = self.text
        file = self.file
        tk = self.tk
        if path.isfile(file):
            file = open(file, 'r')
            for line in file:
                text.insert(tk.END, line + '\n')


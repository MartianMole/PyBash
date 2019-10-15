import os


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


class Ls:
    def __init__(self, keys, currentPath):
        self.keys = keys
        self.currentPath = currentPath

    def makeKeysList(self):
        keys = self.keys
        result = []
        for i in keys:
            if i[0] == '-':
                for j in i[1:]:
                    result.append(j)
        return result

    def showList(self):
        keys = Ls.makeKeysList(self)
        currentPath = self.currentPath
        result = ''
        listDir = os.listdir(currentPath)
        for i in range(len(os.listdir(currentPath))):
            if listDir[i][0] == '.' and 'a' in keys or listDir[i][0] != '.':
                result += listDir[i] + ' '
        if 'l' not in keys:
            return result
        if 'l' in keys:  # Then it shows type(file or folder) and size in bytes
            result = ''
            j = 1
            for i in range(len(listDir)):
                if listDir[i][0] == '.' and 'a' in keys or listDir[i][0] != '.':
                    result += (str(j) + ') ' + listDir[i]).ljust(30, '_') + \
                              (str('folder') * os.path.isdir(str(currentPath + '/' + listDir[i]).replace('\\', '/')) +
                               str('file') * os.path.isfile(
                                          str(currentPath + '/' + listDir[i]).replace('\\', '/'))).ljust(10, '_') + \
                              str(os.stat(str(currentPath + '/' + listDir[i]).replace('\\', '/')).st_size) + '\n'
                    j += 1
        return result

import os
import makeKeysList
import makePath


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
    def __init__(self, keys, currentPath, requestPath=os.getcwd()):
        self.keys = keys
        self.currentPath = currentPath
        self.requestPath = requestPath

    def showList(self):
        keys = makeKeysList.makeKeysList(self.keys, 'alh')
        currentPath = self.currentPath
        requestPath = self.requestPath
        result = ''
        if requestPath != os.getcwd():
            listDir = os.listdir('\\'.join(makePath.processingRequest(requestPath, currentPath)))
            currentPath = '\\'.join(makePath.processingRequest(requestPath, currentPath))
        else:
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

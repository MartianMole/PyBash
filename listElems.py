import os


__doc__ = '''
=============ls=============
Command showing list of directories and files
==> Usage:
ls [keys]
==> Keys:
-h help
-a
==> Examples: 
=============ls=============
'''


class Ls:
    def __init__(self, keys, currentCwd):
        self.keys = keys
        self.currentCwd = currentCwd

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
        currentCwd = self.currentCwd
        result = ''
        listDir = os.listdir(currentCwd)
        for i in range(len(os.listdir(currentCwd))):
            if listDir[i][0] == '.' and 'a' in keys or listDir[i][0] != '.':
                result += listDir[i] + ' '
        if 'l' not in keys:
            return result
        if 'l' in keys:
            result = ''
            j = 1
            for i in range(len(listDir)):
                if listDir[i][0] == '.' and 'a' in keys or listDir[i][0] != '.':
                    result += (str(j) + ') ' + listDir[i]).ljust(30, '_') + \
                              (str('folder') * os.path.isdir(str(currentCwd + '/' + listDir[i]).replace('\\', '/')) +
                               str('file') * os.path.isfile(
                                          str(currentCwd + '/' + listDir[i]).replace('\\', '/'))).ljust(10, '_') + \
                              str(os.stat(str(currentCwd + '/' + listDir[i]).replace('\\', '/')).st_size) + '\n'
                    j += 1
        return result

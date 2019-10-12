from os import path

__doc__ = '''
=============cd=============
Command to navigate directories
==> Usage:
cd _path_
Use .. to navigate up one directory
==> Examples: 
cd Desktop\\Folder
cd ..\\OtherFolder
=============cd=============
'''


class ChangeDirectory:
    def __init__(self, command, currentCwd):
        self.command = command
        self.currentCwd = currentCwd

    def processingRequest(self):
        command = self.command
        currentCwd = self.currentCwd.split('\\')
        separatedCommand = command[1].split('\\')
        if '' in separatedCommand[:-1]:  # In cases like cd ..\\\Folder\\
            return "Error: wrong request"
        j = 0
        while j < len(separatedCommand) and separatedCommand[j] == '..':  # Go up the directories
            if len(currentCwd) > 1:
                print(currentCwd)
                currentCwd.pop()
            j += 1
        for i in range(j, len(separatedCommand)):
            if path.exists('\\'.join(currentCwd + [separatedCommand[i]])) and \
                    path.isdir('\\'.join(currentCwd + [separatedCommand[i]])):
                currentCwd.append(separatedCommand[i])  # Making new Path List
            else:
                return "Error: wrong request"
        return currentCwd

    def doTheThing(self):
        if len(self.command) == 2:
            return ChangeDirectory.processingRequest(self)
        else:
            return 'Error: wrong command'

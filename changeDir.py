from os import path

__doc__ = '''
================cd================
Command to navigate directories

==> Usage:
cd [path]
Use .. to navigate up one directory

==> Examples:
cd Desktop:
    C:\\Desktop
cd ..
    C:\\
================cd================
'''


class ChangeDirectory:
    def __init__(self, command, currentPath):
        self.command = command
        self.currentPath = currentPath

    def processingRequest(self):
        command = self.command
        currentPath = self.currentPath.split('\\')
        separatedCommand = command[1].split('\\')
        if '' in separatedCommand[:-1]:  # In cases like cd ..\\\Folder\\
            return "Error: wrong request"
        j = 0
        while j < len(separatedCommand) and separatedCommand[j] == '..':  # Go up the directories
            if len(currentPath) > 1:
                print(currentPath)
                currentPath.pop()
            j += 1
        for i in range(j, len(separatedCommand)):
            if path.exists('\\'.join(currentPath + [separatedCommand[i]])) and \
                    path.isdir('\\'.join(currentPath + [separatedCommand[i]])):
                currentPath.append(separatedCommand[i])  # Making new Path List
            else:
                return "Error: wrong request"  # Cases like "fol der" will be added in future
        return currentPath

    def doTheThing(self):
        if len(self.command) == 2:
            return ChangeDirectory.processingRequest(self)
        else:
            return 'Error: wrong command'

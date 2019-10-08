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

    def doTheThing(self):
        command = self.command
        currentCwd = self.currentCwd.split('\\')
        if len(command) == 1:
            return __doc__
        elif len(command) == 2:
            separatedCommand = command[1].split('\\')
            while '' in separatedCommand:  # In cases like 'cd ..\\\\Folder\\\'
                separatedCommand.pop(separatedCommand.index(''))
            j = 0
            while j < len(separatedCommand) and separatedCommand[j] == '..':
                if len(currentCwd) > 1:
                    currentCwd.pop()
                j += 1


            #### ИСПРАВИТЬ
            for i in range(j, len(separatedCommand)):
                if path.isdir('\\'.join(currentCwd + [separatedCommand[i]])) and \
                        path.exists('\\'.join(currentCwd + [separatedCommand[i]])):
                    currentCwd.append(separatedCommand[i])  # Making new Path List
                else:
                    return "Error: you can't move to the file"
            if path.exists('\\'.join(currentCwd)):
                return currentCwd
            else:
                return "Error: path doesn't exist"
            #### ИСПРАВИТЬ



        else:
            return 'Error: wrong command'

from os import path


class ChangeDirectory:
    def __init__(self, command, currentCwd):
        self.command = command
        self.currentCwd = currentCwd

    def doTheThing(self):
        command = self.command
        currentCwd = self.currentCwd.split('\\')
        if len(command) == 1:
            return 'SomeDocumentation'
        elif len(command) == 2:
            separatedCommand = command[1].split('\\')
            while '' in separatedCommand:  # In cases like 'cd ..\\\\Folder\\\'
                separatedCommand.pop(separatedCommand.index(''))
            j = 0
            while j < len(separatedCommand) and separatedCommand[j] == '..':
                if len(currentCwd) > 1:
                    currentCwd.pop()
                j += 1
            for i in range(j, len(separatedCommand)):
                currentCwd.append(separatedCommand[i])
            if path.exists('\\'.join(currentCwd)):
                return currentCwd
            else:
                return 'Error'
        else:
            return 'Error'

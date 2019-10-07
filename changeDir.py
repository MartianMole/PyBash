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
            for i in range(len(separatedCommand)):
                if separatedCommand[i] == '..' and i == 0:
                    if len(currentCwd) > 1:
                        currentCwd.pop()
        return currentCwd

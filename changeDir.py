from os import path
import makePath

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

    def doTheThing(self):
        if len(self.command) == 2:
            if path.isdir('\\'.join(makePath.processingRequest(self.command[1], self.currentPath))):
                return makePath.processingRequest(self.command[1], self.currentPath)
            else:
                return None
        else:
            return 'Error: wrong command'

from os import path

__doc__ = r'''
This module just makes the full path from command like ..\..\folder\file
'''


def processingRequest(request, currentPath):
    currentPath = currentPath.split('\\')
    separatedRequest = request.split('\\')
    if '' in separatedRequest[:-1]:  # In cases like cd ..\\\Folder\\
        return "Error: wrong request"
    j = 0
    while j < len(separatedRequest) and separatedRequest[j] == '..':  # Go up the directories
        if len(currentPath) > 1:
            currentPath.pop()
        j += 1
    for i in range(j, len(separatedRequest)):
        if path.exists('\\'.join(currentPath + [separatedRequest[i]])):
            currentPath.append(separatedRequest[i])  # Making new Path List
        else:
            return "Error: wrong request"  # Cases like "fol der" will be added in future
    return currentPath

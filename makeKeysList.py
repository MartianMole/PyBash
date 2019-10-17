def makeKeysList(keys, validValues):
    result = []
    for i in keys:
        if i[0] == '-':
            for j in i[1:]:
                if j in validValues:
                    result.append(j)
                else:
                    return 'Error: unknown key ' + j
    return result

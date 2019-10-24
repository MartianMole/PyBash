def makeKeysList(keys, validValues):
    result = set()
    for i in keys:
        if i[0] == '-':
            for j in i[1:]:
                if j in validValues:
                    result.add(j)
                else:
                    return 'Error: unknown key ' + j
    return result

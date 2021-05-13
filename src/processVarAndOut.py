from re import match
from re import findall

def getVarsFromBlock(rawData):

    dictValue = {}

    for line in rawData:

        # Do nothing if empty line
        if line == '\n':
            continue

        if match('^variable\s+\".+\"\s{', line):
            dictValue['name'] = findall('^variable\\s"(.+)\"\s{', line)[0]

        if match('\s+description\s+', line):
            dictValue['description'] = findall('description\s+\=\s+\"(.+)\"', line)[0]

        if match('\s+type\s+', line):
            dictValue['type'] = findall('type\s+\=\s+(\w*)', line)[0]

        if match('\s+default\s+', line):
            dictValue['default'] = findall('\s+default\s+\=\s+(.+)', line)[0]

        if match('\s+sensitive\s+', line):
            dictValue['sensitive'] = findall('sensitive\s+\=\s+(.+)', line)[0]

        if match('^output\s+\".+\"\s{', line):
            dictValue['name'] = findall('^output\\s"(.+)\"\s{', line)[0]

        if match('\s+value\s+', line):
            dictValue['value'] = findall('\s+value\s+=\s+(.+)', line)[0]

    return dictValue

    #TODO add support for objects, maps

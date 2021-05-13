from re import match
from re import findall

def getVarsFromBlock(rawVar):

    mapVars = {}

    for line in rawVar:

        # Do nothing if empty line
        if line == '\n':
            continue

        # Check if start variable definition and get variable name
        if match('^variable\s+\".+\"\s{', line):
            mapVars['name'] = findall('^variable\\s"(.+)\"\s{', line)[0]

        if match('\s+description\s+', line):
            mapVars['description'] = findall('description\s+\=\s+\"(.+)\"', line)[0]

        if match('\s+type\s+', line):
            mapVars['type'] = findall('type\s+\=\s+(\w*)', line)[0]

        if match('\s+default\s+', line):
            mapVars['default'] = findall('\s+default\s+\=\s+(.*)', line)[0]

        if match('\s+sensitive\s+', line):
            mapVars['sensitive'] = findall('sensitive\s+\=\s+(.+)', line)[0]

    return mapVars

    #TODO add support for objects, maps
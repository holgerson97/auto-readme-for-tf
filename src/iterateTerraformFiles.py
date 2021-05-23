from re import match, findall, search
import os
import pprint

def captureTerraformObjects(path):

    def lookupFiles():
        '''
        Returns list of Terraform files in given script param "args.path".  
        '''

        tfFiles = []

        for file in os.listdir(path):
            if file.endswith(".tf"):
                tfFiles.append(file)

        return tfFiles

    def captureCurlyBraces(file, line):
        '''
        Get everything between to curly braces. Used to hanlde Terraform syntax.
        '''

        # Used for iteration in while loop.
        count = -1
        # Store everythin between curly braces to return it.
        block = ''
        # Number of opend and not yet closed braces.
        braces = 0

        while(True):
            count += 1

            # Skip if empty line
            if file[line + count] == "\n": continue

            # Count all braces in line
            for i in file[line + count]:
                if i == '{':
                    braces += 1
                elif i == '}':
                    braces -= 1

            # Add the line to block.
            block += file[line + count]

            # End if all braces are closed and Terraform object has been captured.
            if braces == 0:
                break
        
        return block

    def createVariable(tfObject):
        '''
        Create a dict for every variable found in each Terraform file.
        Returns each dict to add it to the global dictionary.
        '''
        varObject = {}

        # Get variable name from tfObject
        try:
            tfName = findall('^variable\\s"(.+)\"\s{', tfObject)[0]
            varObject.update({'name' : tfName})
        except (ValueError,IndexError):
           print('Variable name not found for:\n' + tfObject) + "\n Please make sure, that your configuration is valid."

        # Get description from tfObject
        try:
            tfDescription = findall('description\s+\=\s+\"(.+)\"', tfObject)[0]
            varObject.update({'description' : tfDescription})
        except (ValueError,IndexError):
            # Since descriptions are optional we can pass IndexErrors
            pass

        # Get type from tfObject
        try:
            tfType = findall('type\s+=\s+([\w\W]*\}\))|type\s+=\s+([\w()]+)', tfObject)[0]
            if tfType[0] == '': 
                varObject.update({'type' : tfType[1].replace('\n', '')})
            elif tfType[1] == '':
                varObject.update({'type' : tfType[0].replace('\n', '')})
        except (ValueError,IndexError):
            # Since types are optional we can pass IndexErrors
            pass

        # Get default from tfObject
        try:
            tfDefault = findall('default\s+=\s({[\w\s=\"{}]*})|default\s+\=\s+\"*([\w()]*)\"*', tfObject)[0]
            if tfDefault[0] == '': 
                varObject.update({'default' : tfDefault[1].replace('\n', '')})
            elif tfDefault[1] == '':
                varObject.update({'default' : tfDefault[0].replace('\n', '')})
        except (ValueError,IndexError):
            # Since defaults are optional we can pass IndexErrors
            pass

        # Get sensitive from tfObject
        try:
            tfSensitive = findall('sensitive\s+\=\s+(.+)', tfObject)[0]
            varObject.update({'sensitive' : tfSensitive})
        except (ValueError,IndexError):
            # Since sensitives are optional we can pass IndexErrors
            pass

        return varObject

    def createOutput(tfObject):
        '''
        Create a dict for every output found in each Terraform file.
        Returns each dict to add it to the global dictionary.
        '''
        
        outObject = {}

        # Get output name from tfObject
        try:
            tfName = findall('^output\\s"(.+)\"\s{', tfObject)[0]
            outObject.update({'name' : tfName})
        except (ValueError,IndexError):
           print('Output name not found for:\n' + tfObject) + '\n Please make sure, that your configuration is valid.'

        # Get description from tfObject
        try:
            tfDescription = findall('description\s+\=\s+\"(.+)\"', tfObject)[0]
            outObject.update({'description' : tfDescription})
        except (ValueError,IndexError):
            # Since descriptions are optional we can pass IndexErrors
            pass

        # Get value from tfObject
        try:
            tfValue = findall('\s+value\s+=\s+(.+)', tfObject)[0]
            outObject.update({'Value' : tfValue})
        except (ValueError,IndexError):
            raise print('Value not specified for output object:\n' + tfObject + '\n Please make sure, that your configuration is valid.')

        # Get sensitive from tfObject
        try:
            tfSensitive = findall('sensitive\s+\=\s+(.+)', tfObject)[0]
            outObject.update({'sensitive' : tfSensitive})
        except (ValueError,IndexError):
            # Since sensitives are optional we can pass IndexErrors
            pass

        return outObject

    def createVersion(tfObject):
        '''
        Create a dict for every version statement found in each Terraform file.
        Returns each dict to add it to the global dictionary.
        '''

        verObject = { 'TerraformVersion' : '', 'Modules' : [] }

        # Get required Terraform version name from tfObject
        try:
            tfVersion = findall('required_version\s=\s\"(.*)\"', tfObject)[0]
            verObject.update({'TerraformVersion' : tfVersion})
        except (ValueError,IndexError):
           # Since Terraform version statement is optional we can pass IndexErrors
           pass

        # Get provider names from tfObject
        try:
            tfProviderName = findall('\n\s{4}(\w+)', tfObject)
            for i in range(0, len(tfProviderName)):
                verObject['Modules'].append({'Name' : tfProviderName[i] })
        except:
            pass

        # Get provider source from tfObject
        try:
            tfProviderSource = findall('\n\s{6}source\s+=\s+\"(.*)\"', tfObject)
            for i in range(0, len(tfProviderSource)):
                verObject['Modules'][i].update({ 'source' : tfProviderSource[i] })
        except:
            # Since Terraform source statement is optional we can pass IndexErrors
            pass
        
        # Get provider version from tfObject
        try:
            tfProviderVersion = findall('\n\s{6}version\s+=\s+\"(.*)\"', tfObject)
            for i in range(0, len(tfProviderVersion)):
                verObject['Modules'][i].update({ 'version' : tfProviderVersion[i] })
        except:
            # Since Terraform version statement is optional we can pass IndexErrors
            pass

        return verObject

    def getTerraformObjects(tfFile):
        '''
        Iterate through Terraform files and get all objects.
        '''
        tfLines = (open(path + '/' + tfFile, 'r')).readlines()
             
        for i in range(0, len(tfLines)):

            if match('^variable\s\".+\"\s{', tfLines[i]):
                tfVar = captureCurlyBraces(tfLines, i)
                struc['variables'].append(createVariable(tfVar))

            elif match('^output\s\".+\"\s{', tfLines[i]):
                tfOut = captureCurlyBraces(tfLines, i)
                struc['outputs'].append(createOutput(tfOut))

            elif match('^terraform\s+{', tfLines[i]):
                tfVersion = captureCurlyBraces(tfLines, i)
                struc['versions'].append(createVersion(tfVersion))
      
    struc = { 'variables' : [], 'outputs' : [], 'versions' : [] }

    for i in lookupFiles():
        getTerraformObjects(i)

    return struc
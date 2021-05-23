from re import match, findall
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
        Returns each dict to add it to the global disctionary.
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
                varObject.update({'type' : tfType[1]})
            elif tfType[1] == '':
                varObject.update({'type' : tfType[0]})
        except (ValueError,IndexError):
            # Since types are optional we can pass IndexErrors
            pass

        # Get default from tfObject
        try:
            tfDefault = findall('default\s+=\s+([\w\W]*\}\))|default\s+=\s+([\w()]+)', tfObject)[0]
            if tfDefault[0] == '': 
                varObject.update({'type' : tfDefault[1]})
            elif tfDefault[1] == '':
                varObject.update({'type' : tfDefault[0]})
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

    def getTerraformObjects(tfFile):
        '''
        Iterate through Terraform files and get all objects.
        '''
        tfLines = (open(path + '/' + tfFile, 'r')).readlines()
             
        for i in range(0, len(tfLines)):

            if match('^variable\s\".+\"\s{', tfLines[i]):
                tfVar = captureCurlyBraces(tfLines, i)
                struc['variables'].append(tfVar)

            elif match('^output\s\".+\"\s{', tfLines[i]):
                pass

            elif match('^terraform\s+{', tfLines[i]):
                pass
      
    struc = { 'variables' : [], 'outputs' : [], 'versions' : [] }

    for i in lookupFiles():
        getTerraformObjects(i)

    pprint.pprint(struc)
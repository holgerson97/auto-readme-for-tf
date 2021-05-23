from re import match
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
        
    def getTerraformObjects(tfFile):
        '''
        Iterate through Terraform files and get all objects.
        '''
        tfLines = (open(path + '/' + tfFile, 'r')).readlines()
        
        for i in range(0, len(tfLines)):

            if match('^variable\s\".+\"\s{', tfLines[i]):
                tfVar = captureCurlyBraces(tfLines, i)
                print(tfVar)

            elif match('^output\s\".+\"\s{', tfLines[i]):
                pass

            elif match('^terraform\s+{', tfLines[i]):
                pass

    
    for i in lookupFiles():
        getTerraformObjects(i)

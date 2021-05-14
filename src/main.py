import argparse
import subprocess
import os
from re import match

import processVarAndOut
import renderReadMe

from pprint import pprint

def getBlock(tfFile, struc):

    tfLines = (open(args.path + '/' + tfFile, 'r')).readlines()

    for i in range(0, len(tfLines)):
        line = tfLines[i]

        block = []

        if match('^variable\s\".+\"\s{', line):
            if line[-2] == '}':
                block.append(line)
                continue

            count = -1

            while(True):
                count +=1
                block.append(tfLines[i + count])

                if tfLines[i + count][0] == '}':
                    break

            struc['variables'].append(block)
          


        if match('^output\s\".+\"\s{', line):
            
            if line[-1] == '}':
                block + line
                continue

            count = -1

            while(True):
                count +=1
                block.append(tfLines[i + count])

                if tfLines[i + count][0] == '}':
                    break
            
            struc['outputs'].append(block)

def lookupFiles():
    '''
    Returns list of Terraform files in given script param "args.path".  
    '''

    tfFiles = []

    for file in os.listdir(args.path):
        if file.endswith(".tf"):
            tfFiles.append(file)

    return tfFiles

def main():

    subprocess.call("./preflight.sh" + ' -p ' + args.path, shell=True)

    struc = { 'variables' : [], 'outputs' : [] }

    # Get all variables and outputs defined in Terraform conifguration. Save them to strc dict.
    for file in lookupFiles():
        getBlock(file, struc)

    # Build an array of maps that contain information about variables.
    resultVars = []
    for tfVars in struc['variables']:
        resultVars.append(processVarAndOut.getVarsFromBlock(tfVars))

    # Build an array of maps that contain information about outputs.
    resultOuts = []
    for tfOuts in struc['outputs']:
        resultOuts.append(processVarAndOut.getVarsFromBlock(tfOuts))

    with open(args.path + '/README.md', 'w') as file:
        file.write(renderReadMe.render(args.name, resultVars, resultOuts, args.contribute))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--path', type=str, default='./module',
                        help='Specify path to your Terraform module directory. Defaults to "./module".')

    parser.add_argument('--name', type=str, default='default_name',
                        help='Specify the name of your Terraform module. Defaults to "default_name".')

    parser.add_argument('--contribute', type=bool, default=True,
                        help='Choose if you want to accept PRs. Defaults to True.')

    global args
    args = parser.parse_args()

    main()
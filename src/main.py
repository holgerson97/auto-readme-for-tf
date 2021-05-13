import argparse
import subprocess
import os
from re import match

import processVarAndOut

from pprint import pprint

def getBlock(tfFile, struc):

    tfLines = (open(args.path + '/' + tfFile, 'r')).readlines()

    for i in range(0, len(tfLines)):
        line = tfLines[i]

        block = []

        if match('^variable\s\".+\"\s{', line):

            if line[-1] == '}':
                block + line
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

    # Build an array of maps that contain infomration about variables.
    resultVars = []

    for tfVars in struc['variables']:
        resultVars.append(processVarAndOut.getVarsFromBlock(tfVars))

    pprint(resultVars)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--path', type=str, default='./module',
                        help='Specify path to your Terraform module directory. Defaults to "./module".')

    global args
    args = parser.parse_args()

    main()
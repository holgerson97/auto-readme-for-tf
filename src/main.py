import argparse
import re
from pprint import pprint

def getVariablesFile():
    tfVarsFile = open(args.path + '/variables.tf', 'r')

    tfVarsLines = tfVarsFile.readlines()

    varStruc = {}

    for i in range(0, len(tfVarsLines)):
        line = tfVarsLines[i]

        print(line)

        if line == "\n":
            continue

        if 'variable' in line:
            varName = (re.findall('".+?"', line)[0]).replace('"', "")
            varStruc.update({"name" : varName})
           
        if 'description' in line:
            varDescription = ((re.findall('\=(.*)', line)[0]).replace(" ", "")).replace('"', "")
            varStruc.update({"description" : varDescription})

        if 'type' in line:
            varType = (re.findall('\=(.*)', line)[0]).replace(" ", "")
            varStruc.update({"type" : varType})

        if 'default' in line:
            varDefault = re.findall('\=(.*)', line)[0]

            if '{' in varDefault:
                varDefault = {}
                while True:
                    i = i + 1
                    value = tfVarsLines[i]
                    if '}' in value:
                        break
                    varDefault.update({(re.findall('[^=]*', value)[0]).replace(" ","") : (re.findall('\=(.*)', value)[0]).replace(" ","")})
            
            varStruc.update({"default" : varDefault})    

        if 'sensitive' in line:
            varSensitive = (re.findall('\=(.*)', line)[0]).replace(" ", "")
            varStruc.update({"sensitive" : varSensitive})    

    pprint(varStruc)

def main():
    getVariablesFile()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--path', type=str, default='./module',
                        help='Specify path to your Terraform module directory. Defaults to "./module".')

    args = parser.parse_args()

    main()
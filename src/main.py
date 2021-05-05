import argparse
import re

def getVariablesFile():
    tfVarsFile = open(args.path + '/variables.tf', 'r')

    tfVarsLines = tfVarsFile.readlines()

    for line in tfVarsLines:
        if 'variable' in line:
            varName = re.findall('".+?"', line)[0]
            print(varName)
           
        if 'description' in line:
            varDescription = re.findall('\=(.*)', line)[0]
            print(varDescription)

        if 'type' in line:
            varType = re.findall('\=(.*)', line)[0]
            print(varType)

        if 'default' in line:
            varDefault = re.findall('\=(.*)', line)[0]
            print(varDefault)

        if 'sensitive' in line:
            varSensitive = re.findall('\=(.*)', line)[0]
            print(varSensitive)

def main():
    getVariablesFile()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--path', type=str, default='./module',
                        help='Specify path to your Terraform module directory. Defaults to "./module".')

    args = parser.parse_args()

    main()
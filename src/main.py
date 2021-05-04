import argparse

def getVariablesFile():
    tfVarsFile = open(args.path + '/variables.tf', 'r')

    tfVarsLines = tfVarsFile.readlines()

    for line in tfVarsLines:
        if 'variable' in line:
            pass




def main():
    pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--path', type=str, default='./module',
                        help='Specify path to your Terraform module directory. Defaults to "./module".')

    args = parser.parse_args()

    main()
import argparse
import subprocess
import os
from re import match, findall
import pprint

import processVarAndOut
import renderReadMe
import iterateTerraformFiles

def main():

    subprocess.call("./preflight.sh" + ' -p ' + args.path, shell=True)

    struc = { 'variables' : [], 'outputs' : [], 'versions' : [] }

    iterateTerraformFiles.captureTerraformObjects(args.path)

    # Build an array of maps that contain information about variables.
    # resultVars = []
    # for tfVars in struc['variables']:
    #     resultVars.append(processVarAndOut.getVarsFromBlock(tfVars))

    # # Build an array of maps that contain information about outputs.
    # resultOuts = []
    # for tfOuts in struc['outputs']:
    #     resultOuts.append(processVarAndOut.getVarsFromBlock(tfOuts))
    
    # resultVersions = []
    # for tfVersions in struc['versions']:
    #     resultVersions.append(processVarAndOut.getVarsFromBlock(tfVersions))

    # with open(args.path + '/README.md', 'w') as file:
    #     file.write(renderReadMe.render(args.name, resultVars, resultOuts, args.contribute))


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
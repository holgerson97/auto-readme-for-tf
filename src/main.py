#!/usr/bin/python3
import argparse
import subprocess
import renderReadMe
import iterateTerraformFiles
import getContentFromExistingREADME

def main():

    subprocess.call("./preflight.sh" + ' -p ' + args.path, shell=True)

    struc = iterateTerraformFiles.captureTerraformObjects(args.path)

    title = getContentFromExistingREADME.captureTitle(args.path)
    description = getContentFromExistingREADME.captureDescription(args.path)
    gettingStartedBasic = getContentFromExistingREADME.captureGettingStartedBasic(args.path)
    gettingStartedAdvanced = getContentFromExistingREADME.captureGettingStartedAdvanced(args.path)
    badges = getContentFromExistingREADME.captureBadges(args.path)

    with open(args.path + '/README.md', 'w') as file:
        file.write(
            renderReadMe.render(
                badges,
                title,
                description,
                args.tableofcontents,
                args.requirements,
                args.gettingstarted,
                gettingStartedBasic,
                gettingStartedAdvanced,
                struc['versions'],
                struc['resources'],
                args.resources,
                struc['variables'],
                args.variables,
                struc['outputs'],
                args.outputs,
                args.contribute))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--path',
        type=str,
        default='../tests',
        help='Specify path to your Terraform module directory. \
              Defaults to "../tests".')

    parser.add_argument(
        '--tableofcontents',
        type=bool,
        default=True,
        help='Choose if you want to display a table of contents. \
              Defaults to true.')

    parser.add_argument(
        '--resources',
        type=bool,
        default=True,
        help='Choose if you want to display resources. \
              Defaults to true.')

    parser.add_argument(
        '--variables',
        type=bool,
        default=True,
        help='Choose if you want to display a variables. \
              Defaults to true.')

    parser.add_argument(
        '--outputs',
        type=bool,
        default=True,
        help='Choose if you want to display a outputs. \
              Defaults to true.')

    parser.add_argument(
        '--requirements',
        type=bool,
        default=True,
        help='Choose if you want to display a requirements. \
              Defaults to true.')

    parser.add_argument(
        '--gettingstarted',
        type=bool,
        default=True,
        help='Choose if you want to display a getting-started. \
              Defaults to true.')

    parser.add_argument(
        '--contribute',
        type=bool,
        default=True,
        help='Choose if you want to accept PRs. \
              Defaults to True.')

    global args
    args = parser.parse_args()

    main()

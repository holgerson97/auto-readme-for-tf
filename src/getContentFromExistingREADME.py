def captureTitle(path):
    '''
    Inputs: Path to the Terraform Module
    Returns: Title from existing README file.
    '''

    mdLines = (open(path + 'README.md', 'r')).readlines()
    
    return mdLines[0][:-1]

def captureDescription(path):
    '''
    Inputs: Path to the Terraform Module
    Returns: Description from existing README file.
    '''

    mdLines = (open(path + 'README.md', 'r')).readlines()
    description = []
    
    for i in range(0, len(mdLines)):

        if mdLines[i] == '&nbsp;\n':
            break
        elif i == 0:
            continue
        else:
            description.append(mdLines[i][:-1])

    return description

def captureGettingStartedBasic(path):
    '''
    Inputs: Path to Terraform Module
    Returns: Getting Started basic usage block form README file.
    '''

    mdLines = (open(path + 'README.md', 'r')).readlines()
    gettingStarted = []

    for i in range(0, len(mdLines)):

        if mdLines[i] == '## Basic usage\n':
            while True:
                i += 1 

                if mdLines[i] == '## Advanced usage\n':
                    break
                
                gettingStarted.append(mdLines[i][:-1])

    return gettingStarted


def captureGettingStartedAdvanced(path):
    '''
    Inputs: Path to Terraform Module
    Returns: Getting Started advanced usage blocks form README file.
    '''

    mdLines = (open(path + 'README.md', 'r')).readlines()
    gettingStarted = []

    for i in range(0, len(mdLines)):

        if mdLines[i] == '## Advanced usage\n':
            while True:
                i += 1 
                if mdLines[i] == '&nbsp;\n':
                    break
    
                gettingStarted.append(mdLines[i][:-1])

    return gettingStarted
from jinja2 import Environment, FileSystemLoader


def render(
        title,
        description,
        tableOfContents,
        requirements,
        gettingStarted,
        gettingStartedBasic,
        gettingStartedAdvanced,
        versions,
        res,
        resStatement,
        vars,
        varsstatement,
        outs,
        outsstatement,
        contribute):

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('readme.j2')
    renderdReadMe = template.render(
        title=title,
        description=description,
        tableOfContents=tableOfContents,
        requirements=requirements,
        gettingStarted=gettingStarted,
        gettingStartedBasic=gettingStartedBasic,
        gettingStartedAdvanced=gettingStartedAdvanced,
        terraformVersion=versions[0],
        versions=versions[0]['Modules'],
        resources=res,
        resourcesStatement=resStatement,
        variables=vars,
        varsstatement=varsstatement,
        outputs=outs,
        outsstatement=outsstatement,
        contribute=contribute)

    return renderdReadMe

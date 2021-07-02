from jinja2 import Environment, FileSystemLoader


def render(
        moduleName,
        tableOfContents,
        requirements,
        gettingStarted,
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
        name=moduleName,
        tableOfContents=tableOfContents,
        requirements=requirements,
        gettingStarted=gettingStarted,
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

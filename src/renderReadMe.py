from jinja2 import Environment, FileSystemLoader

def render(moduleName, vars, outs, contribute):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('readme.j2')
    renderdReadMe = template.render(name = moduleName, variables = vars, outputs = outs, contribute = contribute)
    print(renderdReadMe)
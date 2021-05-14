from jinja2 import Environment, FileSystemLoader

def render(vars, outs):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('readme.j2')
    renderdReadMe = template.render(variables = vars, outputs = outs)
    print(renderdReadMe)
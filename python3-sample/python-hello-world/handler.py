from jinja2 import Template
import json

def handle(req):
    input = json.loads(req)

    t = Template("Hello {{name}}")
    res = t.render(name=input["name"])
    return res



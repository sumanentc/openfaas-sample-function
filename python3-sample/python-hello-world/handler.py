from jinja2 import Template

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    t = Template("Hello {{name}}")
    res = t.render(name="Jane")
    return res



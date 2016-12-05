from pygments import highlight
from pygments.lexers import PythonLexer
from ..parsons import CustomHtmlFormatter


def problem():
    with open('./problem.py', 'r') as file:
        code = file.read()
        html = highlight(code, PythonLexer(), CustomHtmlFormatter())

    problem = []
    i = 0
    for line in html.splitlines():
        tabs, html = line.split('##')
        problem.append((i, html.strip(), int(tabs) // 4))
        i += 1

    return problem

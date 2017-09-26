# 2017 Daniel Stotts
from sanic.response import html, HTTPResponse, text
from jinja2 import Environment, FileSystemLoader
from os.path import dirname
from sys import modules

DIR_BASE = dirname(modules['__main__'].__file__)
j2 = Environment(loader=FileSystemLoader(DIR_BASE), enable_async=True)


async def html_render(path: str, replace: dict = None) -> HTTPResponse:
    if replace is None:
        replace = {}

    return html(await j2.get_template(path).render_async(replace))

# 2017 Daniel Stotts
from sanic import Sanic
from sanic.response import text, redirect, file
from subprocess import check_output

from api.html import html_render

site = Sanic()


@site.route("/")
async def index(_):
    # return text("This is a test!")
    return redirect("/toys/cubic")


@site.route("/static/<path:path>")
async def static(_, path):
    return await file("static/{}".format(path))


@site.route("/python/<path:path>", methods=["POST"])
async def python(request, path):
    out = check_output(["python3", "static/py/{}".format(path), *(list(request.form.values())[0])],
                       universal_newlines=True)
    return text(str(out))


@site.route("/toys/cubic")
async def cubic(_):
    return html_render("template/cubic.html")


@site.route("/minecraft")
async def minecraft(_):
    return html_render("template/minecraft.html")


@site.route("/mc")
async def mc(_):
    return await redirect("/minecraft")


@site.route("/test")
async def test(_):
    return text("Another test!")


@site.route("/html", methods=["GET", "POST"])
async def htmltest(request):
    return html_render("template/index.html", {
        "test": "Template value!",
        "printed": request.form.get("textboxtest"),
    })


if __name__ == "__main__":
    site.run(host="0.0.0.0", port=80)

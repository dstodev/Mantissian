# 2017 Daniel Stotts
from sanic import Sanic
from sanic.response import text, redirect, file

from api.html import html_render

site = Sanic()


@site.route("/")
async def index(_):
    # return text("This is a test!")
    return redirect("/minecraft")


@site.route("/static/<path:path>")
async def static(_, path):
    return await file("static/{}".format(path))


@site.route("/minecraft")
async def minecraft(_):
    return await html_render("template/minecraft.html")


@site.route("/mc")
async def mc(_):
    return await redirect("/minecraft")


@site.route("/test")
async def test(_):
    return await text("Another test!")


@site.route("/html", methods=["GET", "POST"])
async def htmltest(request):
    return await html_render("template/index.html", {
        "test": "Template value!",
        "printed": request.form.get("textboxtest"),
    })


if __name__ == "__main__":
    site.run(host="0.0.0.0", port=80)

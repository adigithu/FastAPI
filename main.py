from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates=Jinja2Templates(directory="Templates")
posts: list[dict]=[
    {
        "id": 1,
        "author": "Aditya J Parida",
        "title": "FastAPI",
    },
    {
        "id": 2,
        "author": "Pratyush Panda",
        "title": "Python",
    },
]

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html", {"posts": posts, "title": "Home"},
    )
@app.get("/api/posts")
def get_posts():
    return posts
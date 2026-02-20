from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI for Clean, Fast APIs",
        "content": "FastAPI makes it easy to design clean endpoints with automatic docs and strong typing.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Designing Readable Endpoints",
        "content": "A good API reads like a sentence: clear nouns, predictable verbs, and consistent paths.",
        "date_posted": "April 21, 2025",
    },
    {
        "id": 3,
        "author": "Alex Kim",
        "title": "Structured Responses Win Trust",
        "content": "Consistent response shapes reduce client bugs and make your API easier to adopt.",
        "date_posted": "April 22, 2025",
    },
    {
        "id": 4,
        "author": "Samira Patel",
        "title": "Keep Templates Boring",
        "content": "Push logic into Python and keep templates focused on structure and presentation.",
        "date_posted": "April 23, 2025",
    },
    {
        "id": 5,
        "author": "Luis Moreno",
        "title": "Caching the Right Things",
        "content": "Cache expensive queries and rendered pages, but avoid caching user-specific data.",
        "date_posted": "April 24, 2025",
    },
    {
        "id": 6,
        "author": "Priya Nair",
        "title": "Logs That Actually Help",
        "content": "Log request IDs, durations, and status codes so you can trace problems quickly.",
        "date_posted": "April 25, 2025",
    },
    {
        "id": 7,
        "author": "Jordan Lee",
        "title": "Testing the Happy Path First",
        "content": "Start with simple success cases, then add edge cases once the core flow is solid.",
        "date_posted": "April 26, 2025",
    },
    {
        "id": 8,
        "author": "Maya Singh",
        "title": "Make Pagination Predictable",
        "content": "Stable ordering and explicit limits give clients consistent results across requests.",
        "date_posted": "April 27, 2025",
    },
]


@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html", context={"posts": posts, "title": "Home"}
    )


@app.get("/api/posts")
def get_posts():
    return {"posts": posts}

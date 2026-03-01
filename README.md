# fastapi-blog

FastAPI blog app with a JSON API and server-rendered pages.

## What It Does
- Create, update, and delete users
- Create, update, and delete blog posts
- Render web pages for posts using Jinja templates

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- Jinja2
- SQLite

## Run Locally

### Option 1: `uv` (recommended)
```bash
uv sync
uv run fastapi dev
```

### Option 2: `pip`
```bash
python -m venv .venv
source .venv/bin/activate
pip install "fastapi[standard]" sqlalchemy jinja2
fastapi dev
```

App: `http://127.0.0.1:8000`  
API docs: `http://127.0.0.1:8000/docs`

## Main Endpoints
- `/api/users`
- `/api/posts`

## License
Unlicensed

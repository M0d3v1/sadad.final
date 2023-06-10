import os
from django.core.wsgi import get_wsgi_application
from django.conf import settings
from fastapi import FastAPI

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sadad.settings")
django_app = get_wsgi_application()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/news")
def get_news():
    from news.models import News
    news = News.objects.all()
    news_list = [{"title": item.title, "content": item.content} for item in news]
    return {"news": news_list}

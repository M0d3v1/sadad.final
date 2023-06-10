from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .forms import NewsForm
import sqlite3


def news_list(request):
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})

def news_search(request):
    query = request.GET.get('query')
    news = News.objects.filter(content__icontains=query)
    return render(request, 'news_list.html', {'news': news})

def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news_list.html', {'form': form})

def news_edit(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm(instance=news)
    return render(request, 'news_list.html', {'form': form, 'news': news})

def news_delete(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('news_list')
    return render(request, 'news_list.html', {'news': news})

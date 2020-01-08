from django.shortcuts import render
from news.models import Category, Article
from django.core.paginator import Paginator


def index(request):
    items = Article.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'news/index.html', context)


def article_list(request, category_id):
    cat_title = Category.objects.filter(pk=category_id)
    list_article = Article.objects.filter(article_category=category_id)
    context = {
        'title': cat_title,
        'list_article': list_article
    }
    return render(request, 'news/article_list.html', context)


def content_view(request, category_id, article_id):
    article_content = Article.objects.get(pk=article_id)
    context = {
        'category_id': category_id,
        'article_id': article_id,
        'content': article_content,
    }
    return render(request, 'news/article_content.html', context)


def search_items(request, keyword):
    items = Article.objects.filter(article_title__contains=keyword)
    context = {
        'items': items
    }
    return render(request, 'news/search_result.html', context)

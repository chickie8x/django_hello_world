from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('<category_id>/', views.article_list, name='article_list'),
    path('<category_id>/<article_id>/', views.content_view, name='content_view'),
    path('search/', views.search_items, name='search_items'),
]

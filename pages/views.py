from django.shortcuts import render

from foods.models import Food
from news.models import News
# Create your views here.

def index(request):
    foods = Food.objects.order_by('-list_date').filter(is_published=True)[:4]
    news = News.objects.all()

    context = {
        'foods': foods,
        'news': news
    }

    return render(request, 'pages/index.html', context)


def search(request):
    queryset_list = Food.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    context = {
        'food': queryset_list
    }

    return render(request, 'pages/search.html', context)



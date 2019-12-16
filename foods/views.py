from django.shortcuts import render

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Food
# Create your views here.
def index(request):
    foods = Food.objects.all()

    paginator = Paginator(foods, 4)
    page = request.GET.get('page')
    paged_foods = paginator.get_page(page)

    context = {
        'foods': paged_foods
    }

    return render(request, 'pages/foods.html', context)

def search(request):
    queryset_list = Food.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(title__icontains=keywords)

    context ={
        'foods': queryset_list
    }

    return render(request, 'pages/search.html', context)
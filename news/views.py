from django.shortcuts import render

# Create your views here.
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import News

# Create your views here.
def index(request):
    new = News.objects.all()

    paginator = Paginator(new, 4)
    page = request.GET.get('page')
    paged_foods = paginator.get_page(page)

    context = {
        'new': paged_foods
    }

    return render(request, 'pages/foods.html', context)

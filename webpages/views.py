from unicodedata import category
from django.shortcuts import render
from .models import MyWallz
# Create your views here.


def home(request):
    wallpapers = MyWallz.objects.all()
    featured = MyWallz.objects.filter(is_trending=True)
    category_search = MyWallz.objects.values_list(
        'category', flat=True)
    for_what_search = MyWallz.objects.values_list(
        'for_what', flat=True)
    for_what_search = set(for_what_search)
    category_search = set(category_search)
    dwallpapers = MyWallz.objects.filter(for_what='Desktop')
    mwallpapers = MyWallz.objects.filter(for_what='Mobile')
    twallpapers = MyWallz.objects.filter(for_what='Tablet')
    data = {
        'wallpapers': wallpapers,
        'featured': featured,
        'category_search': category_search,
        'dwallpapers': dwallpapers,
        'mwallpapers': mwallpapers,
        'twallpapers': twallpapers,
        'for_what_search': for_what_search,
    }
    return render(request, 'webpages/home.html', data)


def search(request):
    wallpapers = MyWallz.objects.order_by('-created_at')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            wallpapers = wallpapers.filter(title__icontains=keyword)
    category_search = MyWallz.objects.values_list(
        'category', flat=True).distinct()
    if 'category' in request.GET:
        category = request.GET['category']

        if category == '--Category--':
            wallpapers = wallpapers.all()
        elif category:
            wallpapers = wallpapers.filter(category__iexact=category)

    for_what_search = MyWallz.objects.values_list(
        'for_what', flat=True).distinct()
    if 'for_what' in request.GET:
        for_what = request.GET['for_what']
        if for_what == '--Device--':
            wallpapers = wallpapers.all()
        elif for_what:
            wallpapers = wallpapers.filter(for_what__iexact=for_what)
    data = {
        'wallpapers': wallpapers,
        'keyword': keyword,
        'category_search': category_search,
        'category': category,
        'for_what_search': for_what_search,
        'for_what': for_what,
    }
    return render(request, 'webpages/search.html', data)

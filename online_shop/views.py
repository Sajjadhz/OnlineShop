import itertools

from django.shortcuts import render, redirect

from products.models import Product
from sliders.models import Slider
from site_settings.models import SiteSettings


# header code behind using render partial
def header(request, *args, **kwargs):
    site_setting = SiteSettings.objects.first()
    context = {
        'site_setting': site_setting
    }
    # here we do not need to include app name and templates directory name to address html templates files
    return render(request, 'shared/Header.html', context)


# footer code behind using render partial
def footer(request, *args, **kwargs):
    site_setting = SiteSettings.objects.first()
    context = {
        'site_setting': site_setting
    }
    # here we do not need to include app name and templates directory name to address html templates files
    return render(request, 'shared/Footer.html', context)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


# code behind
def home_page(request):
    sliders = Slider.objects.all()
    most_visit_products = Product.objects.order_by('-visit_count').all()[:8]
    print(most_visit_products)
    latest_products = Product.objects.order_by('-id').all()[:8]
    print(latest_products)
    context = {
        'data': 'new data',
        'sliders': sliders,
        'most_visit': my_grouper(4, most_visit_products),
        'latest_products': my_grouper(4, latest_products),
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    site_setting = SiteSettings.objects.first()
    context = {
        'site_setting': site_setting
    }
    return render(request, 'about_page.html', context)

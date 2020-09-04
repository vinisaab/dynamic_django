from django.shortcuts import render
from .models import Page


def index(request):
    return render(request, 'creator/index.html')


def page(request, target):
    item = Page.objects.get(page=target)

    context = {
        'page': item
    }

    return render(request, 'creator/page.html', context)

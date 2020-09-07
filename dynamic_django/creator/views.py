from django.shortcuts import render
from .models import Page, Sections, Content


def index(request):
    return render(request, 'creator/index.html')


def page(request, target):
    item = Page.objects.get(page=target)
    sec = Sections.objects.filter(page=item)
    cont = Content.objects.filter(page=item)

    context = {
        'page': item,
        'sections': sec,
        'content': cont,
    }

    return render(request, 'creator/page.html', context)

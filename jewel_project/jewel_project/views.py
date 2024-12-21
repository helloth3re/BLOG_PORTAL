from django.shortcuts import render
from jewel_app.models import Article, Categories,Banner
from random import shuffle



def HOME(request):
    banner = list(Banner.objects.all())
    shuffle(banner)

    articles = list(Article.objects.all())
    shuffle(articles)

    articles_latest = Article.objects.all().order_by('-created_date')  # Replace 'date' with your actual field name

    context = {
        'banner' : banner,
        'articles': articles,
        'articles_latest': articles_latest,
    }
    return render(request, 'main/home.html', context)

def CAT(request):
    articles = list(Article.objects.all())
    shuffle(articles)

    categories = Categories.objects.all()

    category_id = request.GET.get('category_id')
    if category_id:
        articles = Article.objects.filter(cat_id=category_id)
    else:
        articles = Article.objects.all()


    context = {
        'articles': articles,
        'categories': categories,
    }
    return render(request, 'main/category.html', context)

def CONT(request):
    return render(request, 'main/contact.html')

def GALL(request):
    return render(request, 'main/gallery.html')

def BASE(request):
    return render(request, 'main/base.html')
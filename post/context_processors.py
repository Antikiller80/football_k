import datetime

from django.db.models import Q

from post.models import Category, Article


def category(request):
    categors = Category.objects.all()
    return {"categors": categors}


def article(request):
    arti = Article.objects.all()[0:8]
    return {"arti": arti}

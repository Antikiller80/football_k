

from post.models import Category, Article


def category(request):
    categors = Category.objects.all()
    return {"categors": categors}


def article(request):
    arti = Article.objects.all()[0:8]
    return {"arti": arti}


"""
A set of request processors that return dictionaries to be merged into a
template context. Each function takes the request object as its only parameter
and returns a dictionary to add to the context.
These are referenced from the setting TEMPLATE_CONTEXT_PROCESSORS and used by
RequestContext.
"""

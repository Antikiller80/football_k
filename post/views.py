from django.shortcuts import render, redirect
from .models import Article, Category, Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from .forms import CommentForm
from django.contrib import auth
from django.contrib.auth.models import User


def detail_category(request, id=None):
    category = Category.objects.get(id=id)
    context = {'category': category}
    return render(request, 'blog/detail_category.html', context)


def detail_article(request, id=None):
    comment_form = CommentForm
    args = {}
    args ['article'] = Article.objects.get(id=id)
    args ['comments'] = Comments.objects.filter(comments_aricle_id=id)
    args ['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render(request, 'blog/detail_article.html', args)


def index_2(request):
    artiii = Article.objects.all()
    paginator = Paginator(artiii, 4)
    page = request.GET.get('page')
    try:
        artiii = paginator.page(page)
    except EmptyPage:
        artiii = paginator.page(1)
    except PageNotAnInteger:
        artiii = paginator.page(1)
    context = {'artiii': artiii}
    return render(request, 'blog/index_2.html', context)


def addlike(request, id):
    try:
        if id in request.COOKIES: #проверка куки файлов, если есть инфа, то просто обновление
            redirect('/')
        else: # нету инфы - добавляется лайк
            article = Article.objects.get(id=id)
            article.likes +=1
            article.save()
            response = redirect('/')
            response.set_cookie(id, 'test')
            print(response)
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def addcomment(request, id=None):
    if request.POST and ("pause" not in request.session): #добавление комментария с разницой в 1 минуту через сессию
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_aricle = Article.objects.get(id=id)
            comment.comments_user_id = auth.get_user(request).id
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/post/article/%s/' % id)

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from articles.models import Article, User


def show_articles(request):
    template = 'articles.html'
    articles = Article.objects.all()
    context = {'articles': articles,
               'status': request.user.paid_content}
    return render(
        request,
        template, context
    )


@login_required
def show_article(request, id):
    article = Article.objects.get(id=id)
    context = {'article': article}
    return render(
        request,
        'article.html', context=context
    )


def get_paid(request):
    template = 'get_paid.html'
    some_user = request.user
    if request.method == 'POST':
        print('====  вход в ПОСТ')
        if request.user.paid_content:
            some_user.paid_content = False
            some_user.save()
        else:
            some_user.paid_content = True
            some_user.save()
    context = {'status': request.user.paid_content}
    return render(
        request,
        template, context
    )

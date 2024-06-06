from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from blog.data import posts

# Create your views here.
def example(request: HttpRequest) -> HttpResponse:
    context = { 'head_title': 'Blog - Articles' }
    if request.method == 'GET':
        return HttpResponse(render(request, 'blog/example.html', context ))

def articles(request: HttpRequest) -> HttpResponse:
    context = { 'head_title': 'Blog - Articles', 'posts': posts }
    if request.method == 'GET':
        return HttpResponse(render(request, 'blog/articles.html', context ))

def article(request: HttpRequest, id: int) -> HttpResponse:
    post = next(post for post in posts if post['id'] == id)
    context = { 'head_title': f'Blog - {post['title']}', 'post': post }
    return HttpResponse(render(request, 'blog/article.html', context ))
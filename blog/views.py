from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def articles(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return HttpResponse(render(
                request, 'blog/articles.html', 
                { 'head_title': 'Blog - list of articles' }))

def example(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return HttpResponse(render(
                request, 'blog/example.html', 
                { 'head_title': 'Blog - example page' }))
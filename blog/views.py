from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def articles(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return HttpResponse(render(
                request, 'articles/index.html', 
                { 'head_title': 'Blog - list of articles' }))
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 보기페이지 요청하게 되면 출력되는 내용을 기재한다.
def home(request):
    return HttpResponse('<h1> Notice Home </h1>')

def about(request):
    return HttpResponse('<h1> Notice about page </h1>')

def web01(request):
    return HttpResponse('<h1> notice web01 page </h1>')

def web02(request):
    return HttpResponse('<h1> notice web02 page </h1>')
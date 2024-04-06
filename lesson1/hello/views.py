from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Определяем функцию для того что бы вывести текст на страницу сайта """
    return HttpResponse('Главная')

def profile(request):
    return HttpResponse("profile")

def about(request):
    return HttpResponse("О сайте")
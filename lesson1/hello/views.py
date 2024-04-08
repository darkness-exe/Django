from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Определяем функцию для того что бы вывести текст на страницу сайта """
    return HttpResponse('Главная')

def profile(request):
    return HttpResponse("profile")

def about(request):
    return HttpResponse("О сайте")



from django.http import HttpResponse

def check_ip_user(request):
    user_agent = request.META["HTTP_USER_AGENT"]
    ip = request.META["REMOTE_ADDR"]
    return HttpResponse(f"Проверка IP-адреса... {ip} \n User_Agent {user_agent}")

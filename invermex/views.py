from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

BASE_MODAL_LINKS_DICT = {'text' : "INICIAR SESSION", 'url' : "login.html" }
BASE_MODAL_LINKS_LIST = [ BASE_MODAL_LINKS_DICT ]

BASE = {
    'BASE_TITLE' : "INVERMEX",
    'BASE_MAIN_TITLE' : "INVIERTE SEGURO",
    'BASE_MODAL_LINKS_LIST' : BASE_MODAL_LINKS_LIST
}

def index(request):
    t = get_template('base.html').render(BASE)
    return HttpResponse(t)

def register_client(request):
    t = get_template('register_client.html').render()
    return HttpResponse(t)

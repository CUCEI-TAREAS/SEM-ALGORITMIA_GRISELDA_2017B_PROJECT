from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

BASE_MODAL_LINKS_DICT = {'text' : "INICIAR SESSION", 'url' : "login.html" }
BASE_MODAL_LINKS_LIST = [ BASE_MODAL_LINKS_DICT ]

BASE = {
	'BASE_TITLE' : "INVERMEX",
	'BASE_MAIN_TITLE' : "INVIERTE CON LOS MEJORES",
	'BASE_MODAL_LINKS_LIST' : BASE_MODAL_LINKS_LIST,
	'BASE_MODAL_TITLE' : "INVIERTE CON LOS MEJORES",
	'BASE_MODAL_CLOSE' : "MENU PRINCIPAL",
	'BASE_FOOTER_TITLE' : "INVERMEX",
	'BASE_FOOTER_SUBTITLE' : "INVIERTE CON LOS MEJORES",
	'BASE_FOOTER_MEDIUM' : "REGRESAR ARRIBA",
	'BASE_FOOTER_LAST' : "ALVARREZ RODRIGUEZ JOSHUA ANTONIO / HINOJOSA PACHECO JAAZIEL / RUIZ GARCIA FELIPE DE JESUS"
}

def index(request):
    t = get_template('index.html').render(BASE)
    return HttpResponse(t)

def register_client(request):
    t = get_template('register_client.html').render()
    return HttpResponse(t)

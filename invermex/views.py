from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def index(request):
    t = get_template('index.html')
    html = t.render()
    return HttpResponse(html)

def register_client(request):
    t = get_template('register_client.html')
    html = t.render()
    return HttpResponse(html)

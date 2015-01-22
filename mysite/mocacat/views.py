from django.http import HttpRequest ,HttpResponse
from django.template import Template ,Context
from django.template.loader import get_template

def index(request):
    #t = get_template('index.html')
    #html = t.render(Context({'Context':'hihi-Tim'}))
    t = Template(u'My name is {{name}}')
    html = t.render(Context({'name':'hihi-tim-oooooooyyyyyyyyy'}))

    return HttpResponse(html)


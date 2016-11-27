from django.template.response import TemplateResponse


def login(request):
    context = {}
    return TemplateResponse(request, 'web/index.html', context)

def home(request):
    context = {}
    return TemplateResponse(request, 'web/hala.html', context)
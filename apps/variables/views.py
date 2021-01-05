from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class variables(TemplateView):
    template_name = "teoria/variables/variables.html"

class ejemplo1(TemplateView):
    template_name = "teoria/variables/ejemplos/ejemplo1.html"

class ejemplo2(TemplateView):
    template_name = "teoria/variables/ejemplos/ejemplo2.html"

class ejemplo3(TemplateView):
    template_name = "teoria/variables/ejemplos/ejemplo3.html"

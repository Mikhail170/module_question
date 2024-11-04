from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def first_page(request):
    return render(request, 'func_template.html')


class second_page(TemplateView):
    template_name = 'clas_template.html'

from django.shortcuts import render

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)



# Create your views here.
class HomePageView(TemplateView):
    template_name = 'mob_app/home.html'

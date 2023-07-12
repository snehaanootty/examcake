from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from myapp.models import Cake
from myapp.forms import CakeForm


class CakeAddView(CreateView):
    model=Cake
    form_class=CakeForm
    template_name="cakeadd.html"
    success_url=reverse_lazy("cake-list")

class CakeListView(ListView):
    model=Cake
    form_class=CakeForm
    template_name="cakelist.html"
    context_object_name="cakes"

class CakeDetailView(DetailView):
    model=Cake
    template_name="cakedetail.html"
    context_object_name="cake"

class CakeUpdateView(UpdateView):
    model=Cake
    form_class=CakeForm
    template_name="cakeupdate.html"
    success_url=reverse_lazy("cake-list")


class CakeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Cake.objects.get(id=id).delete()
        return redirect("cake-list")

    

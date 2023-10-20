# <appname>/views.py
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)

from .models import MyCarModel
# from .models import ExampleModel
from .forms import MyCarForm
# from .forms import ExampleForm

def create_view(request):
  context = {}
  form = MyCarForm(request.POST or None)
  if form.is_valid():
    form.save()

  context['form'] = form
  return render(request, "create_view.html", context)


def list_view(request):
  context = {}
  context["dataset"] = MyCarModel.objects.all()

  return render(request, "list_view.html", context)

def detail_view(request, id):
  context = {}
  context["data"] = MyCarModel.objects.get(id = id)

  return render(request, "detail_view.html", context)

# <appname>/views.py

def update_view(request, id):
  context = {}

  obj = get_object_or_404(MyCarModel, id = id)
  form = MyCarForm(request.POST or None, instance = obj)

  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/" + id)
  
  context["form"] = form

  return render(request, "update_view.html", context)



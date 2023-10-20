from django.shortcuts import render

from .models import MyCarModel
# from .models import ExampleModel
from .forms import MyCarForm

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

# <appname>/views.py

def detail_view(request):
  context = {}
  context["data"] = MyCarModel.objects.get(id = id)

  return render(request, "detail_view.html", context)



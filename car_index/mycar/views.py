from django.shortcuts import render

from .models import MyCarModel, ExampleModel
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



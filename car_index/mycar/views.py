# <appname>/views.py
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.views.generic.detail import DetailView

from .models import MyCarModel
from .forms import MyCarForm
import os, requests


def create_view(request):
  context = {}
  form = MyCarForm(request.POST or None)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/")

  context['form'] = form
  return render(request, "create_view.html", context)


def list_view(request):
  context = {}
  context["dataset"] = MyCarModel.objects.all()

  return render(request, "list_view.html", context)


class DetailView(DetailView):
  # context = {}
  # context["data"] = MyCarModel.objects.get(id = id)

  # api_url = 'https://api.api-ninjas.com/v1/cars?model={}'.format()
  api_url = 'https://api.api-ninjas.com/v1/cars?model={"civic"}'
  response = requests.get(api_url, headers={'X-Api-Key': os.environ['API_KEY']})

  template_name="detail_view.html"
  model = MyCarModel
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # context['data'] = MyCarModel.objects.all()
      # context["car_data"] = {"test":"TEST"}
      return context


  # if response.status_code == requests.codes.ok:
  #   context["car_data"] = response.text
  # else:
  #   context["car_data"] = response.status_code, response.text    

  

  # return render(request, "detail_view.html", context)
  

def update_view(request, id):
  context = {}

  obj = get_object_or_404(MyCarModel, id = id)
  form = MyCarForm(request.POST or None, instance = obj)

  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/" + id)
  
  context["form"] = form

  return render(request, "update_view.html", context)


def delete_view(request, id):
  context = {}
  obj = get_object_or_404(MyCarModel, id = id)

  context["data"] = obj

  if request.method == "POST":
    obj.delete()
    return HttpResponseRedirect("/")
  
  return render(request, "delete_view.html", context)



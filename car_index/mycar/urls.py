# <appname>/urls.py

from django.urls import include, path
from . import views

urlpatterns = {
  path('', views.list_view),
  path("create", views.create_view),
}



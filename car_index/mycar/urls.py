# <appname>/urls.py

from django.urls import include, path
from . import views

urlpatterns = {
  path("create", views.create_view),
}



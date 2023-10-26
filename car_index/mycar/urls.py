# <appname>/urls.py

from django.urls import include, path
from . import views

urlpatterns = {
  path('', views.list_view),
  path("create", views.create_view),
  path('<slug:pk>', views.DetailView.as_view(), name="detail_view"),
  path('<int:id>/update', views.update_view),
  path('<int:id>/delete', views.delete_view),
}



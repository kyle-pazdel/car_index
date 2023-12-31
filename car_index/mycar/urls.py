# <appname>/urls.py

from django.urls import include, path
from . import views

urlpatterns = {
  path('create/', views.create_view),
  path('', views.list_view),
  path('<slug:pk>/', views.MyCarDetailView.as_view(), name="detail_view"),
  path('<int:id>/update/', views.update_view),
  path('<int:id>/delete/', views.delete_view),
}



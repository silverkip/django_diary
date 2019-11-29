from django.urls import path, include
from . import views

urlpatterns = [
  path(r'', views.top, name="top"),
  path(r'diaries', views.index, name="entries"),
  path(r'diaries/<int:diary_id>', views.details, name="detail"),
  path(r'diaries/<int:diary_id>/del', views.delete, name="delete"),
  path(r'diaries/<int:diary_id>/edit', views.update, name="update"),
  path(r'diaries/write', views.write, name="write"),
]

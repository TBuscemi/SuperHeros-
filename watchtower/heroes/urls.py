from django.urls import path
from . import views
# from watchtower import heroes

app_name = "heroes"
urlpatterns = [
    path('', views.index, name ='index')
]

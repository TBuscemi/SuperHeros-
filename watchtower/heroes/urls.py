from django.urls import path
from . import views
# from watchtower import heroes

app_name = "heroes"
urlpatterns = [
    path("index", views.index, name="index")
]

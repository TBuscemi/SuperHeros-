from django.urls import path
from . import views
# from watchtower import heroes

app_name = "heroes"
urlpatterns = [
    path('', views.index, name ='index'),
    path('<int:heroes_id>/', views.detail, name='detail'),  
    path('create/', views.create, name='create_hero'),
    path('edit/<int:heroes_id>/', views.edit, name='edit')
]

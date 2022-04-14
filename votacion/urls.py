from django.urls import URLPattern, path

from . import views

app_name = 'votacion'
urlpatterns = [
    #ex : /votacion/
    path('', views.index, name='index'),
    path('<int:region_id>/', views.list_candidatos, name='list_candidatos'),
]
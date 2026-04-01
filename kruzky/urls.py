from django.urls import path
from . import views

urlpatterns = [
    path('', views.zoznam_kruzkov_cool, name='zoznam_kruzkov_cool'),
    path('normal/', views.zoznam_kruzkov, name='zoznam_kruzkov'),
]
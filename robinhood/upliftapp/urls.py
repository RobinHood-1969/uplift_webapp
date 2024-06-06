from django.urls import path
from upliftapp import views


urlpatterns = [
    path('', views.index, name='index'),
]
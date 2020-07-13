from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('by_two', views.increaseByTwo),
    path('choose_increment', views.chooseIncrement),
    path('destroy_session', views.destroySession),
]
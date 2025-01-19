from django.urls import path
from . import views


urlpatterns = [
    path('statesInfo/', views.state_info, name='state_info'),
    path('', views.home, name='home'),
]

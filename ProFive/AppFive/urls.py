from django.urls import path
from . import views

app_name = 'appfive'

urlpatterns = [
    path('home/',views.index,name='home'),
    path('other/',views.other, name='other'),
    path('register/',views.registeration,name = 'register'),
    path('user_login/',views.user_login, name = 'user_login'),
]
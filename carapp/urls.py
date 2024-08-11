
from django.urls import path
from .import views

urlpatterns = [
    path('',views.login, name="login"),
    path('home',views.home, name="home"),
    path('register/',views.register, name="register"),
    path('logout',views.logout, name="logout")
]
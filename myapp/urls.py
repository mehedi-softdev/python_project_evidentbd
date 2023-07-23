from django.urls import path
from myapp import views


urlpatterns = [
    # path defined for registration template
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
]
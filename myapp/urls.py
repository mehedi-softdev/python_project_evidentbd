from django.urls import path
from myapp import views


urlpatterns = [
    # path defined for registration template
    path('', views.registration, name="registration"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
]
from django.urls import path
from myapp import views


urlpatterns = [
    # path defined for registration template
    path('', views.home, name="home"),
    path('accounts/login/', views.login_user, name="login"),
    path('accounts/registration/', views.registration, name="registration"),
    path('accounts/logout/', views.logout_user, name="logout"),

    # khoj the search
    path('khoj_the_search/', views.khoj_the_search, name="khoj_the_search"),
    # api response
    path('api/get_input_values/', views.get_all_input_values, name='get_input_values'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signuppage, name='signuppage'),
    path('loginpage/',views.loginpage, name='loginpage'),
    path('success/',views.success, name='success')
]
from django.urls import path
from encrypt_app import views

app_name = 'encrypt_app'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="user_login"),
]
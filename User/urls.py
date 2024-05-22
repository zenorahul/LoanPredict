from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.register,name='reg'),
    path('login',views.login,name='log'),
    path('pudata', views.pudata, name='pudata'),
    path('prediction',views.prediction,name='pred'),
    #path('logout', views.logout, name="logout")
]
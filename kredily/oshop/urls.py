from django.contrib import admin
from django.urls import path, include
from oshop.views import CustomAuthTokenLogin, ProductMaintain, maintainOrders

# namespace in django
app_name = 'onshop'

urlpatterns = [
    path('login/', CustomAuthTokenLogin.as_view()),
    path('product/', ProductMaintain.as_view()),
    path('product/<int:pid>/', ProductMaintain.as_view()),
    path('history/', maintainOrders.as_view()),
    path('order/<int:pid>/', maintainOrders.as_view()),
]    

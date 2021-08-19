from . import views
from django.urls import path
urlpatterns = [
    path('hello',views.TextFun,name='hello my page'),
    path('index',views.IndexFun,name='index'),
]
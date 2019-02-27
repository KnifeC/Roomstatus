from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('update/<str:device>/',views.update,name='update'),
    path('update',views.update,name='update')
]
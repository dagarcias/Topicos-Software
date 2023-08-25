from django.urls import path
from . import views


urlpatterns=[
    
    path('',views.home,name='home'),
    path('creacion/',views.creacion,name='creacion'),
    path('listado/',views.listado,name='listado'),
    path('eliminar/<str:codigo>/',views.eliminar,name='eliminar')
    
]
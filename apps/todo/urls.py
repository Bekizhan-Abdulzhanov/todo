from django.urls import path

from apps.todo import views 

urlpatterns = [
    path('', views.homepage, name='index'),
    path('create/',views.create,name='create'),
    path('detail/<int:pk>/',views.retrieve,name='detail'),
    path('delete/<int:pk>/',views.destroy,name='delete'),
    path('update/<int:pk>/',views.update,name='update'),
    
]
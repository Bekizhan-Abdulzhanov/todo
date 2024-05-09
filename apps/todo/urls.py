from django.urls import path

from apps.todo import views 

urlpatterns = [
    path('', views.homepage,name='index'),
    path('add/',views.retrieve,name='add'),
    path('update/<int:todo_id>',views.update,name='update'),
    path('delete/<int:todo_id>',views.destroy,name='delete')
]
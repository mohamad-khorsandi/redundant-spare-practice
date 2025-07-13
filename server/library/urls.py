from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getbooks/', views.get_books, name='get_books'),
    path('create/', views.create_book, name='create_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('monitor/', views.monitor, name='monitor'),
    path('monitor/ping/', views.ping, name='ping'),
    path('monitor/crash/', views.crash, name='crash')
]

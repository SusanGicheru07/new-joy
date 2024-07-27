from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('service', views.service, name="service"),

    path('book/classA/', views.booking_roomA, name='book_roomA'),
    path('book/classB/', views.booking_roomB, name='book_roomB'),
    path('book', views.booking, name='book_room'),
    path('payment', views.payment, name='payment'),
    path('guest', views.guest_list, name='guest_list'),
    path('add', views.add_guest, name='add_guest'),



]
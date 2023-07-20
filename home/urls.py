from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about" ),
    path('bookings', views.bookings, name="booking" ),
    path('docters', views.docters, name="docters" ),
    path('contact', views.contact, name="contact"),
    path('staffs',views.staff, name="staffs")
]


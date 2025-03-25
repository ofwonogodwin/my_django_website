from django.urls import path
from.import views

#Listing The URLS

urlpatterns = [
    path('',views.index,name='homepage'),
    path('about/',views.about,name='aboutpage'),
    path('gallery/',views.gallery,name='gallerypage'),
    path('contact/',views.contact,name='contactpage'),
]
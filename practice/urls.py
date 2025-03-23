from django.urls import path
from.import views

#The URL patterns

urlpatterns = [
    path('index/',views.index),
    path('greet/',views.greet),
    path('greet/greeting/',views.greeting),
]
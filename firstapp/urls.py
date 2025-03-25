from django.urls import path,include
from . import views

app_name='firstapp'
urlpatterns = [    
    path('',views.throw),
    path('catch/',views.catch , name='catch'),
]

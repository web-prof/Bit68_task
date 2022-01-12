from django.urls import path
from .views import register,userDetails


app_name = 'accounts'
urlpatterns = [
    path('register/', register.as_view(), name='register'),
    path('userDetails/',userDetails.as_view(),name='userDetails'),

]

from .views import chat
from django.urls import include, path



urlpatterns = [
    path("c/",chat),    
]
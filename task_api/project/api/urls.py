from django.urls import path
from .views import ListLinks, RewieLink

urlpatterns = [
    path("users_list",ListLinks.as_view()),
    path("sing_list/<int:pk>/", RewieLink.as_view())
]
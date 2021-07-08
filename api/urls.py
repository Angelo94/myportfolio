from django.urls import path, include

from api.views import HomeView, SendMessage

urlpatterns = [
    path('home', HomeView.as_view(), name='portfolio-home'),
    path('sendmessage', SendMessage.as_view(), name='sendmessage'),
]
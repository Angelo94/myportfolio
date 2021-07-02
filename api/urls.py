from django.urls import path, include

from api.views import HomeView

urlpatterns = [
    path('home', HomeView.as_view(), name='portfolio-home'),
]
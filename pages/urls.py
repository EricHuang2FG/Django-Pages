from django.urls import path
from .views import HomePageView, AboutPageView, TimePageView

urlpatterns = [
    path("", HomePageView.as_view(), name = 'home'),
    path("about/", AboutPageView.as_view(), name = 'about'),
    path("time/", TimePageView.as_view(), name = 'time'),
]
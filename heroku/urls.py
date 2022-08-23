from django.urls import path

from heroku.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home_page"),
]

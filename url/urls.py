from django.urls import path
from . import views

app_name = 'urls'

urlpatterns = [
    path("index", views.index, name = 'index'),
    path("", views.urlShort, name = "home"),
    path("u/<str:slugs>", views.UrlRedirect, name="redirect"),
]

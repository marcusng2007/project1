from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("entry/<title>", views.entry, name="index"),
    path("create", views.create, name="create"),
    path("search", views.search, name="search"),
    path("?q=<term>", RedirectView.as_view(url="/search/<term>")),
    path("edit/<title>", views.edit, name="edit"),
    path("random", views.random_page, name="random")
]

#Go here to see how to link custom url
#https://stackoverflow.com/questions/32690356/how-to-pass-variable-in-link-to-the-django-view/32692230

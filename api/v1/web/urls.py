from django.urls import path, include, re_path
from api.v1.web import views

app_name = "api_v1_web"

urlpatterns = [
    path("list-events/", views.list_events, name="list_events"),
    path("list-gallery/", views.list_gallery, name="list_gallery"),
    path("contact/", views.contact, name="contact"),
]
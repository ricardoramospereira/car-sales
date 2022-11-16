from django.urls import path
from .views import index, about, cars, service, contact

urlpatterns = [
    path("", index, name='index'),
    path("about/", about, name='about'),
    path("cars/", cars, name='cars'),
    path("service/", service, name='service'),
    path("contact/", contact, name='contact'),
]
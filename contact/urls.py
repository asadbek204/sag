from django.urls import path
from .views import ContactViewSet

urlpatterns = [
    path('contact/', ContactViewSet.as_view({'post': 'post'}), name='contact'),
]
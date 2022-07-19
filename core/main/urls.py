from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeSliderListView.as_view(), name='home')
]
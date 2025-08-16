# URL routes for core views (dashboard, profile, jobs, match/results) (placeholder).
from django.urls import path
from .views.home import home   # <-- import from core/views/home.py

urlpatterns = [
    path('', home, name='home'),
]

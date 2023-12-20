from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.books),
    path('books/<int:book_id>/', views.book_detail),
  
]

# Solution code for urls.py (app-level):
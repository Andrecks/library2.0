from django.urls import path
from .views import home, SignUpView, validate_username, book_form, book_view

urlpatterns = [
    path('', home, name='home'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('validate_username', validate_username, name='validate_username'),
    path('book/add', book_form, name='book_form'),
    path('book/<int:book_id>/', book_view, name='book'),
]
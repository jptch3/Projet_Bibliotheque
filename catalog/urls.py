from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/books/', views.BookListView.as_view(), name='List_book'),
    path('catalog/book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]
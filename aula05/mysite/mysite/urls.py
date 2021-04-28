"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.all_books, name='all_books'),
    path('book_details/<str:id>', views.book_details, name='book_details'),
    path('authors/', views.all_authors, name='all_authors'),
    path('author_details/<str:id>', views.author_details, name='author_details'),
    path('publishers/', views.all_publishers, name='all_publishers'),
    path('publisher_details/<str:id>', views.publisher_details, name='publisher_details'),
    path('books_by_author/<str:id>', views.books_by_author, name='books_by_author'),
    path('authors_by_publisher/<str:id>', views.authors_by_publisher, name='authors_by_publisher'),
    path('booksearch/', views.booksearch, name='booksearch'),
    path('bookquery/', views.bookquery, name='bookquery'),
    path('bookquery_by_infos/', views.bookquery_by_infos, name='bookquery_by_infos'),
    path('authorquery/', views.authorquery, name='authorquery'),
    path('addauthor/', views.addauthor, name='addauthor'),
    path('addpublisher/', views.addpublisher, name='addpublisher'),
    path('addbook/', views.addbook, name='addbook'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/books'), name='logout'),
]

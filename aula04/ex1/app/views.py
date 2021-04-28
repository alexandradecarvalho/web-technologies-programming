from django.db.models import Q
from django.shortcuts import render

from app.forms import *
from app.models import Author, Book, Publisher


# Create your views here.
def all_books(request):
    tparams = {'books': Book.objects.all(), }
    return render(request, 'all_books.html', tparams)


def book_details(request, id):
    tparams = {'book': Book.objects.get(id=id), }
    return render(request, 'book_details.html', tparams)


def all_authors(request):
    tparams = {'authors': Author.objects.all(), }
    return render(request, 'all_authors.html', tparams)


def author_details(request, id):
    tparams = {'author': Author.objects.get(id=id), }
    return render(request, 'author_details.html', tparams)


def all_publishers(request):
    tparams = {'publishers': Publisher.objects.all(), }
    return render(request, 'all_publishers.html', tparams)


def publisher_details(request, id):
    tparams = {'publisher': Publisher.objects.get(id=id), }
    return render(request, 'publisher_details.html', tparams)


def books_by_author(request, id):
    tparams = {'books': Book.objects.all(), 'author': Author.objects.get(id=id), }
    return render(request, 'books_by_author.html', tparams)


def authors_by_publisher(request, id):
    tparams = {'books': Book.objects.all(), 'publisher': Publisher.objects.get(id=id), }
    return render(request, 'authors_by_publisher.html', tparams)


def booksearch(request):
    if 'query' in request.POST:
        query = request.POST['query']
        if query:
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'booklist.html', {'books': books, 'query': query})
        else:
            return render(request, 'booksearch.html', {'error': True})
    else:
        return render(request, 'booksearch.html', {'error': False})


def bookquery(request):
    if request.method == 'POST':
        form = BookQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'booklist.html', {'books': books, 'query': query})
    else:
        form = BookQueryForm()
    return render(request, 'bookquery.html', {'form': form})


def bookquery_by_infos(request):
    if request.method == 'POST':
        form = BookByInfosQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Book.objects.filter(Q(publisher__name__icontains=query) | Q(authors__name__icontains=query))
            return render(request, 'booklist.html', {'books': books, 'query': query})
    else:
        form = BookByInfosQueryForm()
    return render(request, 'bookinfoquery.html', {'form': form})


def authorquery(request):
    if request.method == 'POST':
        form = AuthorQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            authors = Author.objects.filter(name__icontains=query)
            return render(request, 'authorlist.html', {'authors': authors, 'query': query})
    else:
        form = AuthorQueryForm()
    return render(request, 'authorquery.html', {'form': form})


def addauthor(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            new_author = Author(name=name, email=email)
            new_author.save()
            return render(request, 'all_authors.html', {'authors': Author.objects.all()})
    else:
        form = AddAuthorForm()
    return render(request, 'addauthor.html', {'form': form})


def addpublisher(request):
    if request.method == 'POST':
        form = AddPublisherForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']
            website = form.cleaned_data['website']

            new_publisher = Publisher(name=name, city=city, country=country, website=website)
            new_publisher.save()
            return render(request, 'all_publishers.html', {'publishers': Publisher.objects.all()})
    else:
        form = AddPublisherForm()
    return render(request, 'addpublisher.html', {'form': form})


def addbook(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            author = form.cleaned_data['authors']
            publisher = form.cleaned_data['publisher']

            new_book = Book(title=title, date=date, authors=author, publisher=publisher)
            new_book.save()

            return render(request, 'all_books.html', {'books': Book.objects.all()})
    else:
        form = AddBookForm()
    return render(request, 'addbook.html', {'form': form})

from django.shortcuts import render

from app.forms import BookQueryForm
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
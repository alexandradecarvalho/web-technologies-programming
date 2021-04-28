from django import forms
from app.models import Author, Book, Publisher


class BookQueryForm(forms.Form):
    query = forms.CharField(label='Search Books By Title ', max_length=100)


class AuthorQueryForm(forms.Form):
    query = forms.CharField(label='Search Authors By Name ', max_length=100)


class BookByInfosQueryForm(forms.Form):
    query = forms.CharField(label='Search Books By Authors Or Publishers ', max_length=100)


class AddAuthorForm(forms.Form):
    name = forms.CharField(label='Author\'s Name ', max_length=100)
    email = forms.CharField(label='Author\'s Email ', max_length=100)


class AddPublisherForm(forms.Form):
    name = forms.CharField(label='Publisher\'s Name ', max_length=100)
    city = forms.CharField(label='Publisher\'s City ', max_length=100)
    country = forms.CharField(label='Publisher\'s Country ', max_length=100)
    website = forms.CharField(label='Publisher\'s Website ', max_length=1024)


class AddBookForm(forms.Form):
    title = forms.CharField(label='Book\'s Title ', max_length=100)
    date = forms.DateField(label='Book\'s Publishing Date ', widget=forms.SelectDateWidget())
    authors = forms.MultipleChoiceField(label='Book\'s Authors', choices=tuple(
        [(choice, choice) for choice in
         Author.objects.values_list('name', flat=True)]), widget=forms.Select)
    publisher = forms.ChoiceField(label='Book\'s Publisher', choices=tuple(
        [(choice, choice) for choice in
         Publisher.objects.values_list('name', flat=True)]
    ))

from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre

# Create your views here.
def index(request):
    
    # obtenons le total de lignes pour chaque table en BD
    nbre_livre= Book.objects.all().count()
    nbre_auteur= Author.objects.all().count()
    nbre_genre= Genre.objects.all().count()
    nbre_instance_dispo= BookInstance.objects.filter(status__exact='a').count()

    context= {'nbre_livre': nbre_livre , 'nbre_auteur': nbre_auteur, 'nbre_genre': nbre_genre, 'nbre_instance_dispo': nbre_instance_dispo }

    return render(request, 'index.html', context= context)



class BookListView(generic.ListView):
    model = Book
    context_object_name = "book_list"
    queryset= Book.objects.filter(title_icontains= "war")[:5]
    template_name= "book_list.html"

class BookDetailView(generic.DetailView):
    model = Book
    template_name = "detail_view.html" 
    
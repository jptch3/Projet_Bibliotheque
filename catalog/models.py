from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Language(models.Model):
   
    # Le nom des colonnes
    Langue = models.CharField(max_length= 50, help_text='Saisir le nom de la langue')


    # Les metadonnées
    class Meta :
        ordering= ['-Langue']

    # Les methodes 
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self) :
        return self.Langue
    

class Genre(models.Model):

    name= models.CharField(max_length=200, help_text= 'Donner le genre littéraire du livre. ex: Science fiction')
    
    def __str__(self):
        return self.name


class Book(models.Model):

    title= models.CharField(max_length=200, help_text= 'Sair le titre du livre')
    author= models.ForeignKey('Author', on_delete=models.SET_NULL, null= True)
    summary= models.TextField(max_length=1000, help_text='Le resume doit faire 1000 caractères max')
    isbn= models.CharField('ISBN', max_length=13, help_text='13 caractères <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre= models.ManyToManyField('Genre', help_text= 'Selectionner le ou les genre(s) du livre')

    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

class BookInstance(models.Model):
    id= models.UUIDField(primary_key= True, default= uuid.uuid4)
    book= models.ForeignKey('Book', on_delete= models.RESTRICT, null= True)
    imprunt= models.CharField(max_length= 200)
    due_back= models.DateField(null= True, blank= True)

    loan_status= (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status= models.CharField(max_length= 1, choices= loan_status, blank= True, default= 'a', help_text= 'Disponibilité du livre')

    class Meta:
        ordering= ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'
    
class Author(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
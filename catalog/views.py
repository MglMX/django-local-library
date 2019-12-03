from django.shortcuts import render
from django.views import generic
from catalog.models import Book, Author, BookInstance, Genre


# Create your views here.

def index(request):
    """View function for home page of site"""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The all() is implied by default
    num_authors = Author.objects.count()

    # Books that contain the work 'the'
    num_books_with_the = Book.objects.filter(title__icontains="the").count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_with_the': num_books_with_the
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list'  # your own name for the list as a template variable
    template_name = 'catalog/list_of_books.html'  # Specify own template name/location
    paginate_by = 2

    def get_queryset(self):
        return Book.objects.filter(title__icontains='the')[:5]  # Get 5 book containing the title the

    def get_context_data(self, *, object_list=None, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author

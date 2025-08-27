from django.views.generic import CreateView, DetailView, FormView
from viewer.models import Ebook, EbookAuthor
from .forms import EbookForm, EbookAuthorForm

''' ----- EBOOK SECTION -----'''

''' Class used for adding new ebooks to the website'''
class EbookCreateView(CreateView):
    model = Ebook
    form_class = EbookForm
    template_name = 'ebook_create.html'
    success_url = '/'


''' Class used for adding new authors, so it can be later used in ebooks,
in case website owner wants to add ebooks written by differed people'''
class AuthorCreateView(CreateView):
    model = EbookAuthor
    form_class = EbookAuthorForm
    template_name = 'author_create.html'
    success_url = '/'
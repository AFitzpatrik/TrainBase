from django.views.generic import CreateView, DetailView, FormView
from viewer.models import Ebook
from .forms import EbookForm

''' ----- EBOOK SECTION -----'''

# Class used for adding new ebooks to the website
class EbookCreateView(CreateView):
    model = Ebook
    form_class = EbookForm
    template_name = 'ebook_create.html'
    success_url = '/'




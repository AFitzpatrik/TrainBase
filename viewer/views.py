from django.views.generic import CreateView
from viewer.models import Ebook
from .forms import EbookCreateForm


# Create your views here.
''' ----- EBOOK SECTION -----'''

# Class used for adding new ebooks to the website
class EbookCreateView(CreateView):
    model = Ebook
    form_class = EbookCreateForm
    template_name = 'ebook_create.html'
    success_url = '/'



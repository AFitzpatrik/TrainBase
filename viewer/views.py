from django.shortcuts import render
from django.views.generic import CreateView

from viewer.models import Ebook


# Create your views here.
''' ----- EBOOK SECTION -----'''

# Class used for adding new ebooks to the website
class EbookCreateView(CreateView):
    model = Ebook
    fields = '__all__'
    template_name = 'EbookCreateView.html'
    success_url = '/'


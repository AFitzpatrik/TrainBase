from django import forms
from .models import Ebook


class EbookCreateForm(forms.ModelForm):
    class Meta:
        model = Ebook
        fields = ["name",
                  "cover_image",
                  "description",
                  "price_amount",
                  "price_currency",
                  "file",
                  ]

        widgets = {
            "created_at": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M",
            ),
            "updated_at": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M",
            )
        }

        labels = {"name": "Name",
                  "description": "Description",
                  "price_amount": "Price",
                  "price_currency": "Currency",
                  "cover_image": "Cover Image",
                  "file": "E-book File"
                  }
        help_texts = {"name": "Enter name of your E-book",
                      "description": "Enter description of your E-book",
                      "price_amount": "Enter price of your E-book",
                      "price_currency": "Select currency for the price",
                      "cover_image": "Upload a cover image for your E-book",
                      "file": "Upload your E-book file (PDF recommended)"
                      }

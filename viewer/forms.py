from django import forms



class EbookCreateForm(forms.ModelForm):
    class Meta:
        fields = ["name",
                  "cover_image",
                  "created_at"
                  "updated_at",
                  "description",
                  "price_amount",
                  "price_currency",
                  "file"
                  ]

        widgets = {
            "created_at": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            "updated_at": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            )
        }

        labels = {"name": "Name",
                  "description": "Description",
                  "price_amount": "Price",
        }
        help_texts = {"name": "Enter name of your E-book",
                      "description": "Enter description of your E-book",
                      "price_amount": "Enter price of your E-book",
                      }

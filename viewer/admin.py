from django.contrib import admin
from .models import (
    EbookAuthor,
    Ebook,
    EbookImage,
    ExerciseBodyPart,
    ExerciseImage,
    ExerciseVideo,
    Exercise,
)

# Zaregistrovat modely do Adminu
admin.site.register(EbookAuthor)
admin.site.register(Ebook)
admin.site.register(EbookImage)
admin.site.register(ExerciseBodyPart)
admin.site.register(ExerciseImage)
admin.site.register(ExerciseVideo)
admin.site.register(Exercise)

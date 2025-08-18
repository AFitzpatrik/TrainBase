from django.db import models
from django.db.models import ForeignKey, Model, ImageField

# TRAINER SECTION
'''class OwnerTrainer(models.Model):
    This model is used for the owner of the page. The user of this app creates their own SUPER USER account,
    which then takes all information from this model and puts it where it is needed.
    This approach was chosen because you don’t need to enter the information over again.
    
    I Think its redundant for now, maybe regular Superuser with permissions will suffice.
    Will keep this for later, might be usefull for something.
    
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    tel_number=models.CharField(max_length=100)
    e_mail=models.CharField(max_length=100)
'''







# E-BOOK SECTION
class EbookAuthor(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)


class Ebook(models.Model):
    name = models.CharField(max_length=50,unique=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    ebook_author = models.ForeignKey(EbookAuthor,on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Ebook {self.name}'


class EbookImage(models.Model):
    ebook = models.ForeignKey(Ebook,on_delete=models.CASCADE)


# EXERCISE SECTION
class ExerciseBodyPart(models.Model):
    name= models.CharField(max_length=50, unique=True)
    image_target_muscle = models.ImageField(upload_to='images/body_part', default=None, null=False, blank=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Body part {self.pk}'


class ExerciseImage(models.Model):
    image = models.ImageField(upload_to='images/exercises', default=None, null=False, blank=False)

    def __str__(self):
        return f"Exercise image {self.pk}"

    def __repr__(self):
        return f'Exercise Image {self.pk}'

class ExerciseVideo(models.Model):
    video = models.FileField(upload_to='videos/exercises', default=None, null=False, blank=False)

    def __str__(self):
        return f"Exercise video {self.pk}"


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(ExerciseBodyPart, on_delete=models.CASCADE, related_name='exercises')
    description = models.TextField(null=True, blank=True)
    video = models.ForeignKey(ExerciseVideo, null=True, on_delete=models.SET_NULL, related_name='exercises')
    image_exercise = models.ForeignKey(ExerciseImage, null=True, on_delete=models.SET_NULL, related_name='exercises')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Exercise {self.pk}'










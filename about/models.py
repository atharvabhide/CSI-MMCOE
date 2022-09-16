from django.db import models

# Create your models here.
class Member(models.Model):

    def __str__(self) -> str:
        return self.member_name

    member_name = models.CharField(max_length=70)
    member_position = models.CharField(max_length=20)
    member_image = models.ImageField(upload_to = 'images')
    member_linkedIn = models.URLField(max_length=200, blank=True)
    member_github = models.URLField(max_length=200, blank=True)
    
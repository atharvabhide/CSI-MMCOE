from django.db import models

# Create your models here.

class csi_Event(models.Model):

    def __str__(self) -> str:
        return self.event_name

    event_name = models.CharField(max_length=50)
    event_image = models.ImageField(upload_to='images')
    event_description = models.TextField(max_length=500)
    event_link = models.URLField(blank=True)
    event_feeBool = models.BooleanField(default=False)
    event_fee = models.IntegerField(default=0, blank=True)
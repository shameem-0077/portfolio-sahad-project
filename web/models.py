from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="events/images/")
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/images/")

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"

    def __str__(self):
        return str(self.pk)

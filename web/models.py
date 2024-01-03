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


class Contact(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    email = models.EmailField()
    phone_number = models.CharField(max_length=123)
    message = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.first_name

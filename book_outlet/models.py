from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

# Adding one-to-many relationship


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.name}, {self.code}"

    class Meta:
        verbose_name_plural = 'Countries'


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

# Using a nested Meta class to configure various aspects of the Adress model behavior, in this case:  using the verbose_name_plural property to overwrite the plural form of Address entries.
    class Meta:
        verbose_name_plural = 'Address Entries'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # adding a one-to-one relation
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

# custom method
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# return custom method
    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
# author = models.CharField(null=True, max_length=100)
# connecting with the class Auhor using a foreign key(for one_to_many)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name='books')
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
# Adding a many-to-many relation
    published_countries = models.ManyToManyField(Country)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

# Replaced with the prepopulated_fieids value in the admin.py file
    # def save(self, *args, **kwargs):
      #  self.slug = slugify(self.title)
      #  super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}({self.rating})"

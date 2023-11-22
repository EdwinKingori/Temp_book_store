from django.contrib import admin

from .models import Book, Author, Address, Country
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    # automatically generates the slug field and allows the user to edit the slug field
    prepopulated_fields = {"slug": ('title',)}
    list_filter = ('author', 'rating',)
    list_display = ('title', 'author',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)


class CountryAdmin(admin.ModelAdmin):
    # list_filter = ('code',)
    list_display = ('name', 'code',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country, CountryAdmin)

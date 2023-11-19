from django.contrib import admin

from .models import Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    # automatically generates the slug field and allows the user to edit the slug field
    prepopulated_fields = {"slug": ('title',)}
    list_filter = ('author', 'rating',)
    list_display = ('title', 'author',)


admin.site.register(Book, BookAdmin)

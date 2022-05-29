from django.contrib import admin
from .models import Film, DodatkoweInfo, Ocena, Aktor

# Register your models here.
# admin.site.register(Film)
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    # fields = ["tytul", "opis", "rok"] # dzięki tej opcji widzimy w obiekcie wszystkie zadeklarowane pola
    # exclude = ["opis"] # dzięki tej opcji widzimy w obiekcie wszystkie pola poza tym zadeklarowanym
    # dzięki tej opcji widzimy w liście obiektów konkretne parametry
    list_display = ["tytul", "imdb_rating", "rok"]
    list_filter = ["rok"]  # dodaje opcje filtrowania w panelu admina
    # dodaje pole wyszukiwania w panelu admina
    search_fields = ["tytul", "opis"]


admin.site.register(DodatkoweInfo)
admin.site.register(Ocena)
admin.site.register(Aktor)

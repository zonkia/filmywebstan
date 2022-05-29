from django.urls import path
from filmyweb.views import wszystkie_filmy, nowy_film, edytuj_film, usun_film

urlpatterns = [
    path("wszystkie/", wszystkie_filmy, name="wszystkie_ahref"),
    path("nowy/", nowy_film, name="dodaj_film_ahref"),
    path("edytuj/<int:id>", edytuj_film, name="edytuj_film_ahref"),
    path("usun/<int:id>", usun_film, name="usun_film_ahref"),
]

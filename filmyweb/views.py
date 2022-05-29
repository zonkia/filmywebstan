from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse
from .models import Film, DodatkoweInfo, Ocena
from .forms import FilmForm, DodatkoweInfoForm, OcenaForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def wszystkie_filmy(request):
    # return HttpResponse("to jest pierwszy test")

    wszystkie = Film.objects.all()
    #ilosc = len(wszystkie)
    return render(request, "filmy.html", {"filmy": wszystkie})


@login_required
def nowy_film(request):
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None)

    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        # commit=False blokuje wysyłkę do bazy
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()

        return redirect(wszystkie_filmy)

    return render(request, "film_form.html", {"form": form_film,
                                              "form_dodatkowe": form_dodatkowe,
                                              "nowy": True})


@login_required
def edytuj_film(request, id):
    film = get_object_or_404(Film, pk=id)
    oceny = Ocena.objects.filter(film=film)
    try:
        dodatkowe = DodatkoweInfo.objects.get(film=id)
    except:
        dodatkowe = None

    form_film = FilmForm(request.POST or None,
                         request.FILES or None, instance=film)
    form_dodatkowe = DodatkoweInfoForm(
        request.POST or None, instance=dodatkowe)
    form_ocena = OcenaForm(
        request.POST or None)

    if request.method == "POST":
        if "gwiazdki" in request.POST:
            ocena = form_ocena.save(commit=False)
            ocena.film = film
            ocena.save()

    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        # commit=False blokuje wysyłkę do bazy
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()

        return redirect(wszystkie_filmy)

    return render(request, "film_form.html", {"form": form_film,
                                              "form_dodatkowe": form_dodatkowe,
                                              "oceny": oceny, "form_ocena":
                                              form_ocena, "nowy": False})


@login_required
def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, "potwierdz.html", {"film": film})

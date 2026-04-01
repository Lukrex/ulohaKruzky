from django.shortcuts import render
from .models import Kruzok

DEN_PORADIE = {
    'Pondelok': 1,
    'Utorok': 2,
    'Streda': 3,
    'Štvrtok': 4,
    'Piatok': 5,
    'Sobota': 6,
    'Nedela': 7,
}

def zoznam_kruzkov(request):
    kruzky = Kruzok.objects.select_related('veduci').all()
    kruzky = sorted(kruzky, key=lambda k: DEN_PORADIE.get(k.den, 99))
    return render(request, 'kruzky/realzoznam_kruzkov.html', {'kruzky': kruzky})

def zoznam_kruzkov_cool(request):
    kruzky = Kruzok.objects.select_related('veduci').all()
    kruzky = sorted(kruzky, key=lambda k: DEN_PORADIE.get(k.den, 99))
    return render(request, 'kruzky/zoznam_kruzkov.html', {'kruzky': kruzky})
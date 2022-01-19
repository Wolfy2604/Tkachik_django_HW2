from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    lst = []
    with open('data-398-2018-08-30.csv', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lst.append({
                'name': row['Name'],
                'street': row['Street'],
                'district': row['District']
            })
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(lst, 10)
    context_pg = paginator.get_page(page_number)
    context = {
        'page': context_pg,
    }
    return render(request, 'stations/index.html', context)

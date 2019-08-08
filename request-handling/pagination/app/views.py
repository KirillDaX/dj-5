from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import csv
from app.settings import BUS_STATION_CSV
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(BUS_STATION_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print('>>> reader <<<\n')

        bus_stations_list = []
        for item_row in reader:  # нам нужен спсок словарей с данными которые будут выводиться
            bus_stations = {'Name': item_row['Name'], 'Street': item_row['Street'], 'District': item_row['District']}
            bus_stations_list.append(bus_stations)
        #     используем пагинатор для формирования постраничного доступа
        page_num = request.GET.get('page', 1)  # получаем страницу
        page_cut = Paginator(bus_stations_list, 10)
        page = page_cut.get_page(page_num)
        # делаем проверку, моно ли листать туда сюда
        if page.has_next():
            next_page = f'?page={page.next_page_number()}'
        else:
            next_page = ''

        if page.has_previous():
            prev_page = f'?page={page.previous_page_number()}'
        else:
            prev_page = ''
    return render_to_response('index.html', context={
        'bus_stations': page,
        'current_page': page_num,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
    })



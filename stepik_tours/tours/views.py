from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views import View
from random import sample
# Create your views here.
from tours.data import tours, departures


class MainView(View):

    def get(self, request, *args, **kwargs):
        six_tours = sample(tours.keys(), 6)
        random_tours = {k: tours[k] for k in six_tours}
        return render(request, 'tours/index.html', {'random_tours': random_tours})


def departure_view(request, departure):
    dep_tours = {}
    for k, v in tours.items():
        if v.get('departure') == departure:
            dep_tours[k] = tours[k]  # словарь туров выбранного направления

    dep_from = departures.get(departure)  # откуда вылет
    # Формирование краткой статистики туров направления
    list_price = [v.get('price') for v in dep_tours.values()]
    list_nights = [v.get('nights') for v in dep_tours.values()]
    min_pr = '{:,}'.format(min(list_price)).replace(',', ' ')
    max_pr = '{:,}'.format(max(list_price)).replace(',', ' ')
    stat_departure = {'min_pr': min_pr, 'max_pr': max_pr, 'min_nig': min(list_nights),
                      'max_nig': max(list_nights)}
    return render(request, 'tours/departure.html', {"dep_tours": dep_tours, 'dep_from': dep_from,
                                                    'stat_departure': stat_departure})


def tour_view(request, id):
    # Форматирование цены тура
    price_tour = '{:,}'.format(tours.get(id).get('price')).replace(',', ' ')
    # Получаем наименование источника отправления
    dep_from = departures[tours.get(id).get('departure')]
    return render(request, 'tours/tour.html', {"tour": tours[id], 'price_tour': price_tour, 'dep_from': dep_from})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Нет такого тура или маршрута')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')

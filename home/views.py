from django.shortcuts import render
import json
from time import gmtime, strftime


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# Create your views here.
def home(request):
    print(strftime("%d/%m/%Y %H:%M:%S", gmtime()),
          get_ip(request),
          request.build_absolute_uri(),
          file=open('ip.txt', 'a'))
    sets = json.loads(''.join(open('data.json', 'r').readlines()))['sets']
    return render(request, 'home/index.html', {
        'title': 'Stanhome | Rosalina',
        'sets': sets
    })


def dettagli(request, id):
    print(strftime("%d/%m/%Y %H:%M:%S", gmtime()),
          get_ip(request),
          request.build_absolute_uri(),
          file=open('ip.txt', 'a'))
    data = json.loads(''.join(
        [line.decode() for line in open('data.json', 'rb').readlines()]))
    scelto = data['sets'][id]
    prodotti = data['prodotti']
    return render(
        request, 'home/dettagli.html', {
            'title':
            'Stanhome | Set ' + str(id + 1),
            'nome':
            scelto['nome'],
            'img':
            '/' + scelto['img'],
            'prodotti': [prodotti[i] for i in scelto['componenti']],
            'wa_url':
            'https://wa.me/+393395662773/?text=Voglio il set n°' + str(id + 1)
        })

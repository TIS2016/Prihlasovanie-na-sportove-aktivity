from django.template.response import TemplateResponse
from django.template.defaulttags import register
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from web.models import Reservation, Room, Administrator


@register.filter
def multiply(dictionary, value):
    return value * dictionary


times = [
    "08:00-08:30",
    "08:30-09:00",
    "09:00-09:30",
    "09:30-10:00",
    "10:00-10:30",
    "10:30-11:00",
    "11:00-11:30",
    "11:30-12:00",
    "12:00-12:30",
    "12:30-13:00",
    "13:00-13:30",
    "13:30-14:00",
    "14:00-14:30",
    "14:30-15:00",
    "15:00-15:30",
    "15:30-16:00",
    "16:00-16:30",
    "16:30-17:00",
    "17:00-17:30",
    "17:30-18:00",
    "18:00-18:30",
    "18:30-19:00",
]

months = {
    "Jan": '01',
    "Feb": '02',
    "Mar": '03',
    "Apr": '04',
    "May": '05',
    "Jun": '06',
    "Jul": '07',
    "Aug": '08',
    "Sep": '09',
    "Okt": '10',
    "Nov": '11',
    "Dec": '12'
}


def index(request):
    """
    View function to handle Ajax request for image Link.
    :param request: Ajax request data.
    :return: image URL.
    """


# <-----------------------------> HALA <------------------------------------------>
@csrf_exempt
def hala(request):
    room = Room.objects.get(name='hala')
    capacity = room.capacity

    context = {
        "times": times,
        "reservations": Reservation.objects.filter(room=room),
        "capacity": capacity,

    }
    if request.method == 'POST':
        if request.is_ajax():
            # print("DATA", request.POST.get('d1'))

            mon = str(request.POST.get('d1')).strip().split()
            tue = str(request.POST.get('d2')).strip().split()
            wed = str(request.POST.get('d3')).strip().split()
            thu = str(request.POST.get('d4')).strip().split()
            fri = str(request.POST.get('d5')).strip().split()

            # print(months.get(mon[1]), mon[2], mon[3])

            mon = "{}-{}-{}".format(mon[3], months.get(mon[1]), mon[2])
            tue = "{}-{}-{}".format(tue[3], months.get(tue[1]), tue[2])
            wed = "{}-{}-{}".format(wed[3], months.get(wed[1]), wed[2])
            thu = "{}-{}-{}".format(thu[3], months.get(thu[1]), thu[2])
            fri = "{}-{}-{}".format(fri[3], months.get(fri[1]), fri[2])

            result = list()
            for time in times:
                for day_date in [mon, tue, wed, thu, fri]:
                    r = Reservation.objects.filter(date=day_date, time=time, room=room).count()
                    result.append(r)

            response_data = {
                "reservations": result,
                "capacity": capacity,

            }
            return JsonResponse(response_data)

    # Get goes here
    return TemplateResponse(request, 'web/hala.html', context)


def hala_terminy(request):
    context = {
        "terminy": request.POST.getlist('termins_id[]'),
    }
    return TemplateResponse(request, 'web/hala_terminy.html', context)


@csrf_exempt
def hala_termin(request, termin_id):
    context = {
        "termin_id": termin_id,
    }
    if request.is_ajax():
        print("datum", request.POST.get('datum'))

        response_data = {
            "times": times,
            "reservations": [5, 5, 6, 3, 4, 8],
            "pocet": 9,
        }
        return JsonResponse(response_data)

    return TemplateResponse(request, 'web/hala_termin.html', context)


# <-----------------------------> POSILNOVNA <-------------------------------------->
def posilnovna(request):
    context = {
        "times": times,
    }
    return TemplateResponse(request, 'web/posilnovna.html', context)


def posilnovna_terminy(request):
    context = {
        "terminy": request.POST.getlist('termins_id[]'),
    }
    return TemplateResponse(request, 'web/posilnovna_terminy.html', context)


def posilnovna_termin(request, termin_id):
    context = {
        "termin_id": termin_id,
    }
    return TemplateResponse(request, 'web/posilnovna_termin.html', context)


# <-----------------------------> STENA <------------------------------------------>
def stena(request):
    context = {
        "times": times,
    }
    return TemplateResponse(request, 'web/stena.html', context)


def stena_terminy(request):
    context = {
        "terminy": request.POST.getlist('termins_id[]'),
    }
    return TemplateResponse(request, 'web/stena_terminy.html', context)


def stena_termin(request, termin_id):
    context = {
        "termin_id": termin_id,
    }
    return TemplateResponse(request, 'web/stena_termin.html', context)


# <-----------------------------> SAUNA <------------------------------------------>
def sauna(request):
    context = {
        "times": times,
    }
    return TemplateResponse(request, 'web/sauna.html', context)


def sauna_terminy(request):
    context = {
        "terminy": request.POST.getlist('termins_id[]'),
    }
    return TemplateResponse(request, 'web/sauna_terminy.html', context)


def sauna_termin(request, termin_id):
    context = {
        "termin_id": termin_id,
    }
    return TemplateResponse(request, 'web/sauna_termin.html', context)

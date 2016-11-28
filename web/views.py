from django.template.response import TemplateResponse
from django.template.defaulttags import register
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

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

    if request.is_ajax():
        import json

        print("DATA", request.POST.get('d1'))
        print("DATA", request.POST.get('d2'))
        print("DATA", request.POST.get('d3'))
        print("DATA", request.POST.get('d4'))
        print("DATA", request.POST.get('d5'))



        response_data = {
            "times": times,
            "reservations": [5,5,6,3,4,8],
            "capacity": capacity,
        }
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

        # return TemplateResponse(request, 'web/hala.html', response_data)

        # try:
        #     monday_date = request.POST['monday_date']
        #     print("gabaj", monday_date)
        #
        # except:
        #     e = sys.exc_info()
        #     return HttpResponse(e)
        # return HttpResponse(sucess)
        # return TemplateResponse(request, 'web/hala.html', context)
    else:
        # pass
        return TemplateResponse(request, 'web/hala.html', context)


@csrf_exempt
def hala_terminy(request):
    context = {
        "terminy": request.POST.getlist('termins_id[]'),
    }
    return TemplateResponse(request, 'web/hala_terminy.html', context)


def hala_termin(request, termin_id):
    context = {
        "termin_id": termin_id,
    }
    return TemplateResponse(request, 'web/hala_termin.html', context)


# <-----------------------------> POSILNOVNA <-------------------------------------->
def posilnovna(request):
    context = {
        "times": times,
    }
    return TemplateResponse(request, 'web/posilnovna.html', context)


@csrf_exempt
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


@csrf_exempt
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


@csrf_exempt
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

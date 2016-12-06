from django.template.response import TemplateResponse
from django.template.defaulttags import register
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from django.template import Context, loader

from web.models import Reservation, Room, Administrator


@register.filter
def multiply(dictionary, value):
    return value * dictionary


TIMES = [
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

MONTHS = {
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
    "Dec": '12',
}

DAYS = {
    1: "Pondelok",
    2: "Utorok",
    3: "Streda",
    4: "Stvrtok",
    0: "Piatok",
}


# <-----------------------------> HALA <------------------------------------------>
@csrf_exempt
# @ensure_csrf_cookie
def hala(request):
    room = Room.objects.get(name='hala')
    capacity = room.capacity

    context = {
        "times": TIMES,
        "reservations": Reservation.objects.filter(room=room),
        "capacity": capacity,

    }
    if request.method == 'POST':
        if request.is_ajax():
            # print("DATA", request.POST)

            # save new reservations to the database
            if request.POST.get('save'):

                times = request.POST.getlist('times[]')
                notes = request.POST.getlist('notes[]')
                dates = request.POST.getlist('dates[]')

                print("DATES", request.POST)

                for i in range(len(times)):
                    print(times[i], times[i])

                    time = unicode(times[i]).strip().split()

                    Reservation.objects.create(login="user_login", name="user_name", surname="user_surname", room=room,
                                               date=unicode(dates[i]), time=time[1], note=unicode(notes[i]))

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            elif request.POST.get('delete_admin'):

                print("request.POST", request.POST)

                time_date_login = request.POST.getlist('time_date_login[]')

                for i in range(len(time_date_login)):
                    split = time_date_login[i].split(' ')

                    Reservation.objects.filter(login=unicode(split[2]), room=room, date=unicode(split[1]),
                                               time=unicode(split[0])).delete()

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            elif request.POST.get('delete_user'):

                print("request.POST", request.POST)

                time_date_login = request.POST.getlist('time_date_login[]')

                for i in range(len(time_date_login)):
                    split = time_date_login[i].split(' ')

                    Reservation.objects.filter(login=unicode(split[2]), room=room, date=unicode(split[1]),
                                               time=unicode(split[0])).delete()

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            elif request.POST.get('update_user'):

                print("request.POST", request.POST)

                time_date_login = request.POST.getlist('time_date_login[]')
                notes = request.POST.getlist('notes[]')

                for i in range(len(notes)):
                    split = time_date_login[i].split(' ')

                    Reservation.objects.filter(login=unicode(split[2]), room=room, date=unicode(split[1]),
                                               time=unicode(split[0])).update(note=notes[i])

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            elif request.POST.get('get_admin'):

                print("request.POST", request.POST)

                actual_user = request.POST.get('actual_user')

                print(actual_user)

                admins = Administrator.objects.all()
                is_admin = False

                for admin in admins:
                    print(admin.login, actual_user)
                    if admin.login == actual_user:
                        is_admin = True
                        break

                response_data = {
                    "is_admin": is_admin,
                    "message": "DONE",
                }

                return JsonResponse(response_data)

            # send reservations numbers to the view
            else:

                mon = unicode(request.POST.get('d1')).strip().split()
                tue = unicode(request.POST.get('d2')).strip().split()
                wed = unicode(request.POST.get('d3')).strip().split()
                thu = unicode(request.POST.get('d4')).strip().split()
                fri = unicode(request.POST.get('d5')).strip().split()

                # print(months.get(mon[1]), mon[2], mon[3])

                mon = "{}-{}-{}".format(mon[3], MONTHS.get(mon[1]), mon[2])
                tue = "{}-{}-{}".format(tue[3], MONTHS.get(tue[1]), tue[2])
                wed = "{}-{}-{}".format(wed[3], MONTHS.get(wed[1]), wed[2])
                thu = "{}-{}-{}".format(thu[3], MONTHS.get(thu[1]), thu[2])
                fri = "{}-{}-{}".format(fri[3], MONTHS.get(fri[1]), fri[2])

                # print(mon)
                # print(fri)

                result = list()
                for time in TIMES:
                    for day_date in [mon, tue, wed, thu, fri]:
                        r = Reservation.objects.filter(date=day_date, time=time, room=room).count()
                        result.append(r)

                response_data = {
                    "reservations": result,
                    "capacity": capacity,

                }
                return JsonResponse(response_data)  # Get goes here

    return TemplateResponse(request, 'web/hala.html', context)


@csrf_exempt
# @ensure_csrf_cookie
def hala_terminy(request):
    terminy = request.POST.getlist('termins_id[]')
    if request.method == 'POST':
        if request.is_ajax():
            times = list()
            days = list()
            for termin in terminy:
                times.append(TIMES[(int(termin) - 1) // 5])
                days.append(DAYS.get(int(termin) % 5))

            response_data = {
                "res_times": times,
                "res_days": days,
                "number": len(times),
            }
            return JsonResponse(response_data)
            # # Get goes here
            # return TemplateResponse(request, 'web/hala_terminy.html', context)


@csrf_exempt
# @ensure_csrf_cookie
def hala_termin(request, termin_id):
    room = Room.objects.get(name='hala')

    if request.is_ajax():
        print("datum", request.POST.get('date'))

        date = unicode(request.POST.get('date')).strip().split()

        date = "{}-{}-{}".format(date[3], MONTHS.get(date[1]), date[2])
        time = TIMES[(int(termin_id) - 1) // 5]

        res = Reservation.objects.filter(date=date, time=time, room=room)

        res_names = [r.name + " " + r.surname for r in res]
        res_notes = [r.note for r in res]
        res_times = [r.time for r in res]
        res_dates = [r.date for r in res]
        res_logins = [r.login for r in res]

        print("names", res_names)
        print("notes", res_notes)

        response_data = {
            "times": TIMES,
            "res_names": res_names,
            "res_logins": res_logins,
            "res_dates": res_dates,
            "res_times": res_times,
            "res_notes": res_notes,
            "number": res.count(),
        }
        return JsonResponse(response_data)
        # # Get goes here
        # return TemplateResponse(request, 'web/hala_termin.html', context)


# <-----------------------------> POSILNOVNA <-------------------------------------->
@csrf_exempt
def posilnovna(request):
    room = Room.objects.get(name='posilnovna')
    capacity = room.capacity

    context = {
        "times": TIMES,
        "reservations": Reservation.objects.filter(room=room),
        "capacity": capacity,

    }
    if request.method == 'POST':
        if request.is_ajax():
            # print("DATA", request.POST)

            # save new reservations to the database
            if request.POST.get('save'):

                times = request.POST.getlist('times[]')
                notes = request.POST.getlist('notes[]')
                dates = request.POST.getlist('dates[]')

                print("DATES", request.POST)

                for i in range(len(times)):
                    print(times[i], times[i])

                    time = unicode(times[i]).strip().split()

                    Reservation.objects.create(login="user_login", name="user_name", surname="user_surname", room=room,
                                               date=unicode(dates[i]), time=time[1], note=unicode(notes[i]))

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            elif request.POST.get('delete_admin'):

                print("request.POST", request.POST)

                time_date_login = request.POST.getlist('time_date_login[]')

                for i in range(len(time_date_login)):
                    split = time_date_login[i].split(' ')

                    Reservation.objects.filter(login=unicode(split[2]), room=room, date=unicode(split[1]),
                                               time=unicode(split[0])).delete()

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            elif request.POST.get('delete_user'):

                print("request.POST", request.POST)

                time_date_login = request.POST.getlist('time_date_login[]')

                for i in range(len(time_date_login)):
                    split = time_date_login[i].split(' ')

                    Reservation.objects.filter(login=unicode(split[2]), room=room, date=unicode(split[1]),
                                               time=unicode(split[0])).delete()

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            elif request.POST.get('update_user'):

                print("request.POST", request.POST)

                time_date_login = request.POST.getlist('time_date_login[]')
                notes = request.POST.getlist('notes[]')

                for i in range(len(notes)):
                    split = time_date_login[i].split(' ')

                    Reservation.objects.filter(login=unicode(split[2]), room=room, date=unicode(split[1]),
                                               time=unicode(split[0])).update(note=notes[i])

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            # send reservations numbers to the view
            else:

                mon = unicode(request.POST.get('d1')).strip().split()
                tue = unicode(request.POST.get('d2')).strip().split()
                wed = unicode(request.POST.get('d3')).strip().split()
                thu = unicode(request.POST.get('d4')).strip().split()
                fri = unicode(request.POST.get('d5')).strip().split()

                # print(months.get(mon[1]), mon[2], mon[3])

                mon = "{}-{}-{}".format(mon[3], MONTHS.get(mon[1]), mon[2])
                tue = "{}-{}-{}".format(tue[3], MONTHS.get(tue[1]), tue[2])
                wed = "{}-{}-{}".format(wed[3], MONTHS.get(wed[1]), wed[2])
                thu = "{}-{}-{}".format(thu[3], MONTHS.get(thu[1]), thu[2])
                fri = "{}-{}-{}".format(fri[3], MONTHS.get(fri[1]), fri[2])

                # print(mon)
                # print(fri)

                result = list()
                for time in TIMES:
                    for day_date in [mon, tue, wed, thu, fri]:
                        r = Reservation.objects.filter(date=day_date, time=time, room=room).count()
                        result.append(r)

                response_data = {
                    "reservations": result,
                    "capacity": capacity,

                }
                return JsonResponse(response_data)

    # Get goes here
    return TemplateResponse(request, 'web/posilnovna.html', context)


@csrf_exempt
def posilnovna_terminy(request):
    terminy = request.POST.getlist('termins_id[]')
    if request.method == 'POST':
        if request.is_ajax():
            times = list()
            days = list()
            for termin in terminy:
                times.append(TIMES[(int(termin) - 1) // 5])
                days.append(DAYS.get(int(termin) % 5))

            response_data = {
                "res_times": times,
                "res_days": days,
                "number": len(times),
            }
            return JsonResponse(response_data)


@csrf_exempt
def posilnovna_termin(request, termin_id):
    room = Room.objects.get(name='posilnovna')

    if request.is_ajax():
        print("datum", request.POST.get('date'))

        date = unicode(request.POST.get('date')).strip().split()

        date = "{}-{}-{}".format(date[3], MONTHS.get(date[1]), date[2])
        time = TIMES[(int(termin_id) - 1) // 5]

        res = Reservation.objects.filter(date=date, time=time, room=room)

        res_names = [r.name + " " + r.surname for r in res]
        res_notes = [r.note for r in res]
        res_times = [r.time for r in res]
        res_dates = [r.date for r in res]
        res_logins = [r.login for r in res]

        print("names", res_names)
        print("notes", res_notes)

        response_data = {
            "times": TIMES,
            "res_names": res_names,
            "res_logins": res_logins,
            "res_dates": res_dates,
            "res_times": res_times,
            "res_notes": res_notes,
            "number": res.count(),
        }
        return JsonResponse(response_data)


# <-----------------------------> STENA <------------------------------------------>
@csrf_exempt
def stena(request):
    room = Room.objects.get(name='stena')
    capacity = room.capacity

    context = {
        "times": TIMES,
        "reservations": Reservation.objects.filter(room=room),
        "capacity": capacity,

    }
    if request.method == 'POST':
        if request.is_ajax():
            # print("DATA", request.POST)

            # save new reservations to the database
            if request.POST.get('save'):

                times = request.POST.getlist('times[]')
                notes = request.POST.getlist('notes[]')
                dates = request.POST.getlist('dates[]')

                print("DATES", request.POST)

                for i in range(len(times)):
                    print(times[i], times[i])

                    time = unicode(times[i]).strip().split()

                    Reservation.objects.create(login="user_login", name="user_name", surname="user_surname", room=room,
                                               date=unicode(dates[i]), time=time[1], note=unicode(notes[i]))

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            elif request.POST.get('delete_admin'):

                print("request.POST", request.POST)

                time_date_login = request.POST.getlist('time_date_login[]')

                for i in range(len(time_date_login)):
                    split = time_date_login[i].split(' ')

                    Reservation.objects.filter(login=unicode(split[2]), room=room, date=unicode(split[1]),
                                               time=unicode(split[0])).delete()

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            elif request.POST.get('delete_user'):

                print("request.POST", request.POST)

                time_date_login = request.POST.getlist('time_date_login[]')

                for i in range(len(time_date_login)):
                    split = time_date_login[i].split(' ')

                    Reservation.objects.filter(login=unicode(split[2]), room=room, date=unicode(split[1]),
                                               time=unicode(split[0])).delete()

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            elif request.POST.get('update_user'):

                print("request.POST", request.POST)

                time_date_login = request.POST.getlist('time_date_login[]')
                notes = request.POST.getlist('notes[]')

                for i in range(len(notes)):
                    split = time_date_login[i].split(' ')

                    Reservation.objects.filter(login=unicode(split[2]), room=room, date=unicode(split[1]),
                                               time=unicode(split[0])).update(note=notes[i])

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            # send reservations numbers to the view
            else:

                mon = unicode(request.POST.get('d1')).strip().split()
                tue = unicode(request.POST.get('d2')).strip().split()
                wed = unicode(request.POST.get('d3')).strip().split()
                thu = unicode(request.POST.get('d4')).strip().split()
                fri = unicode(request.POST.get('d5')).strip().split()

                # print(months.get(mon[1]), mon[2], mon[3])

                mon = "{}-{}-{}".format(mon[3], MONTHS.get(mon[1]), mon[2])
                tue = "{}-{}-{}".format(tue[3], MONTHS.get(tue[1]), tue[2])
                wed = "{}-{}-{}".format(wed[3], MONTHS.get(wed[1]), wed[2])
                thu = "{}-{}-{}".format(thu[3], MONTHS.get(thu[1]), thu[2])
                fri = "{}-{}-{}".format(fri[3], MONTHS.get(fri[1]), fri[2])

                # print(mon)
                # print(fri)

                result = list()
                for time in TIMES:
                    for day_date in [mon, tue, wed, thu, fri]:
                        r = Reservation.objects.filter(date=day_date, time=time, room=room).count()
                        result.append(r)

                response_data = {
                    "reservations": result,
                    "capacity": capacity,

                }
                return JsonResponse(response_data)

    # Get goes here
    return TemplateResponse(request, 'web/stena.html', context)


@csrf_exempt
def stena_terminy(request):
    terminy = request.POST.getlist('termins_id[]')
    if request.method == 'POST':
        if request.is_ajax():
            times = list()
            days = list()
            for termin in terminy:
                times.append(TIMES[(int(termin) - 1) // 5])
                days.append(DAYS.get(int(termin) % 5))

            response_data = {
                "res_times": times,
                "res_days": days,
                "number": len(times),
            }
            return JsonResponse(response_data)


@csrf_exempt
def stena_termin(request, termin_id):
    room = Room.objects.get(name='stena')

    if request.is_ajax():
        print("datum", request.POST.get('date'))

        date = unicode(request.POST.get('date')).strip().split()

        date = "{}-{}-{}".format(date[3], MONTHS.get(date[1]), date[2])
        time = TIMES[(int(termin_id) - 1) // 5]

        res = Reservation.objects.filter(date=date, time=time, room=room)

        res_names = [r.name + " " + r.surname for r in res]
        res_notes = [r.note for r in res]
        res_times = [r.time for r in res]
        res_dates = [r.date for r in res]
        res_logins = [r.login for r in res]

        print("names", res_names)
        print("notes", res_notes)

        response_data = {
            "times": TIMES,
            "res_names": res_names,
            "res_logins": res_logins,
            "res_dates": res_dates,
            "res_times": res_times,
            "res_notes": res_notes,
            "number": res.count(),
        }
        return JsonResponse(response_data)


# <-----------------------------> SAUNA <------------------------------------------>
@csrf_exempt
def sauna(request):
    room = Room.objects.get(name='sauna')
    capacity = room.capacity

    context = {
        "times": TIMES,
        "reservations": Reservation.objects.filter(room=room),
        "capacity": capacity,

    }
    if request.method == 'POST':
        if request.is_ajax():
            # print("DATA", request.POST)

            # save new reservations to the database
            if request.POST.get('save'):

                times = request.POST.getlist('times[]')
                notes = request.POST.getlist('notes[]')
                dates = request.POST.getlist('dates[]')

                print("DATES", request.POST)

                for i in range(len(times)):
                    print(times[i], times[i])

                    time = unicode(times[i]).strip().split()

                    Reservation.objects.create(login="user_login", name="user_name", surname="user_surname", room=room,
                                               date=unicode(dates[i]), time=time[1], note=unicode(notes[i]))

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            elif request.POST.get('delete_admin'):

                print("request.POST", request.POST)

                time_date_login = request.POST.getlist('time_date_login[]')

                for i in range(len(time_date_login)):
                    split = time_date_login[i].split(' ')

                    Reservation.objects.filter(login=unicode(split[2]), room=room, date=unicode(split[1]),
                                               time=unicode(split[0])).delete()

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            elif request.POST.get('delete_user'):

                print("request.POST", request.POST)

                time_date_login = request.POST.getlist('time_date_login[]')

                for i in range(len(time_date_login)):
                    split = time_date_login[i].split(' ')

                    Reservation.objects.filter(login=unicode(split[2]), room=room, date=unicode(split[1]),
                                               time=unicode(split[0])).delete()

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            elif request.POST.get('update_user'):

                print("request.POST", request.POST)

                time_date_login = request.POST.getlist('time_date_login[]')
                notes = request.POST.getlist('notes[]')

                for i in range(len(notes)):
                    split = time_date_login[i].split(' ')

                    Reservation.objects.filter(login=unicode(split[2]), room=room, date=unicode(split[1]),
                                               time=unicode(split[0])).update(note=notes[i])

                response_data = {
                    "message": "DONE",
                }
                return JsonResponse(response_data)

            # send reservations numbers to the view
            else:

                mon = unicode(request.POST.get('d1')).strip().split()
                tue = unicode(request.POST.get('d2')).strip().split()
                wed = unicode(request.POST.get('d3')).strip().split()
                thu = unicode(request.POST.get('d4')).strip().split()
                fri = unicode(request.POST.get('d5')).strip().split()

                # print(months.get(mon[1]), mon[2], mon[3])

                mon = "{}-{}-{}".format(mon[3], MONTHS.get(mon[1]), mon[2])
                tue = "{}-{}-{}".format(tue[3], MONTHS.get(tue[1]), tue[2])
                wed = "{}-{}-{}".format(wed[3], MONTHS.get(wed[1]), wed[2])
                thu = "{}-{}-{}".format(thu[3], MONTHS.get(thu[1]), thu[2])
                fri = "{}-{}-{}".format(fri[3], MONTHS.get(fri[1]), fri[2])

                # print(mon)
                # print(fri)

                result = list()
                for time in TIMES:
                    for day_date in [mon, tue, wed, thu, fri]:
                        r = Reservation.objects.filter(date=day_date, time=time, room=room).count()
                        result.append(r)

                response_data = {
                    "reservations": result,
                    "capacity": capacity,

                }
                return JsonResponse(response_data)
    # Get goes here
    return TemplateResponse(request, 'web/sauna.html', context)


@csrf_exempt
def sauna_terminy(request):
    terminy = request.POST.getlist('termins_id[]')
    if request.method == 'POST':
        if request.is_ajax():
            times = list()
            days = list()
            for termin in terminy:
                times.append(TIMES[(int(termin) - 1) // 5])
                days.append(DAYS.get(int(termin) % 5))

            response_data = {
                "res_times": times,
                "res_days": days,
                "number": len(times),
            }
            return JsonResponse(response_data)


@csrf_exempt
def sauna_termin(request, termin_id):
    room = Room.objects.get(name='sauna')

    if request.is_ajax():
        print("datum", request.POST.get('date'))

        date = unicode(request.POST.get('date')).strip().split()

        date = "{}-{}-{}".format(date[3], MONTHS.get(date[1]), date[2])
        time = TIMES[(int(termin_id) - 1) // 5]

        res = Reservation.objects.filter(date=date, time=time, room=room)

        res_names = [r.name + " " + r.surname for r in res]
        res_notes = [r.note for r in res]
        res_times = [r.time for r in res]
        res_dates = [r.date for r in res]
        res_logins = [r.login for r in res]

        print("names", res_names)
        print("notes", res_notes)

        response_data = {
            "times": TIMES,
            "res_names": res_names,
            "res_logins": res_logins,
            "res_dates": res_dates,
            "res_times": res_times,
            "res_notes": res_notes,
            "number": res.count(),
        }
        return JsonResponse(response_data)

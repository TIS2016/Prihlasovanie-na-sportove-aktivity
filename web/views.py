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



# login imports
from django.views.generic import View

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from .forms import UserLoginForm, UserRegisterForm

from django.contrib.auth.models import User


# REGISTER
class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'web/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return TemplateResponse(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # way how to chenge password
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/domov/hala/')

        return render(request, self.template_name, {'form': form})


# LOGIN
class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'web/login.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return TemplateResponse(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if not request.user.is_authenticated():
            print("NOT AUTH USER")
            user = authenticate(username=request.POST.get('username'),
                                password=request.POST.get('password'))

            print("NOT AUTH USER", user)



            if user is not None:
                login(request, user)
                print("username", user.username)
                print("first_name", user.first_name)
                print("last_name", user.last_name)
                print("BEFORE REDIRECTTTT")
                return redirect('/domov/hala/')

        else:
            print("AUTH USER")
            user = User.objects.get(id=request.user.id)
            print("AUTHENTIFIKOVANY")
            print("USERNAME",user.username)
            print("FIRST", user.first_name)
            print("LAST", user.last_name)
            print("EMAIL", user.email)


def _logout(request):
    print("PRED ODHLASENIM USER", request.user)
    logout(request)
    return redirect('../')





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
    capacity = 3 #room.capacity

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

                if request.user.is_authenticated():
                    username = request.user.username
                    first_name = request.user.first_name
                    last_name = request.user.last_name
                    print("USERNAME:",username)

                    times = request.POST.getlist('times[]')
                    notes = request.POST.getlist('notes[]')
                    dates = request.POST.getlist('dates[]')



                    print("DATES", request.POST)

                    for i in range(len(times)):
                        print(times[i], times[i])

                        time = unicode(times[i]).strip().split()

                        Reservation.objects.create(login=username, name=first_name, surname=last_name, room=room,
                                                   date=unicode(dates[i]), time=time[1], note=unicode(notes[i]))

                    response_data = {
                        "message": "DONE",
                    }
                    return JsonResponse(response_data)
                else:
                    print("not_authentificated")

            elif request.POST.get('save_block'):

                if request.user.is_authenticated():
                    username = request.user.username
                    first_name = request.user.first_name
                    last_name = request.user.last_name

                    times = request.POST.getlist('times[]')
                    notes = request.POST.getlist('notes[]')
                    dates = request.POST.getlist('dates[]')

                    print("DATES", request.POST)

                    number = None
                    not_empty = False

                    for i in range(len(times)):
                        print(times[i], times[i])

                        time = unicode(times[i]).strip().split()

                        number = Reservation.objects.filter(room=room, date=unicode(dates[i]),time=unicode(time[1])).count()


                        print("NUMBEEEEEEEER", number)

                        if number > 0:
                            not_empty = True

                    if not_empty:
                        response_data = {
                            "message": "DONE",
                            "not_empty": not_empty,
                        }
                        return JsonResponse(response_data)

                    else:
                        for i in range(len(times)):
                            print(times[i], times[i])

                            time = unicode(times[i]).strip().split()

                            Reservation.objects.create(login=username, name=first_name, surname=last_name, room=room,
                                                   date=unicode(dates[i]), time=unicode(time[1]), note=unicode("Zablokovany Termin: " + notes[i]), is_blocked="True")

                        response_data = {
                            "message": "DONE",
                            "not_empty": 0,
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
                if request.user.is_authenticated():
                    username = request.user.username
                    has = False
                    print("request.POST", request.POST)

                    time_date_login = request.POST.getlist('time_date_login[]')

                    for i in range(len(time_date_login)):
                        split = time_date_login[i].split(' ')
                        if split[2] == username:
                            has = True
                            Reservation.objects.filter(login=unicode(split[2]), room=room, date=unicode(split[1]),
                                                   time=unicode(split[0])).delete()

                    response_data = {
                        "message": "DONE",
                        "has": has,
                    }
                    return JsonResponse(response_data)

            elif request.POST.get('update_user'):
                if request.user.is_authenticated():
                    username = request.user.username
                    has = False
                    print("request.POST", request.POST)

                    time_date_login = request.POST.getlist('time_date_login[]')
                    notes = request.POST.getlist('notes[]')

                    for i in range(len(notes)):
                        split = time_date_login[i].split(' ')
                        print("SPLIT2", split[2])
                        if split[2] == username:
                            has = True
                            Reservation.objects.filter(login=unicode(split[2]), room=room, date=unicode(split[1]),
                                                   time=unicode(split[0])).update(note=notes[i])

                    response_data = {
                        "message": "DONE",
                        "has": has,
                    }
                    return JsonResponse(response_data)

            # send reservations numbers to the view
            else:
                if request.user.is_authenticated():
                    is_admin = request.user.is_staff

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
                    blocked = list()
                    for time in TIMES:
                        for day_date in [mon, tue, wed, thu, fri]:
                            r = Reservation.objects.filter(date=day_date, time=time, room=room)
                            result.append(r.count())
                            # print(r.values_list('is_blocked', flat=True))
                            blocked.append(bool(r.values_list('is_blocked', flat=True)))


                    response_data = {
                        "reservations": result,
                        "capacity": capacity,
                        "is_admin": is_admin,
                        "is_blocked": blocked,

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
        if request.user.is_authenticated():
            username = request.user.username
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

            res_allow_update = [r.login == username for r in res]

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
                "res_allow_update" : res_allow_update,
                "is_admin": request.user.is_staff
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

                first = request.POST.get('first_name')
                last = request.POST.get('last_name')
                username = request.POST.get('username')


                print("DATES", request.POST)

                for i in range(len(times)):
                    print(times[i], times[i])

                    time = unicode(times[i]).strip().split()

                    Reservation.objects.create(login=username, name=first, surname=last, room=room,
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

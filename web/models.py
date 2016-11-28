from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=30)
    capacity = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)

    def __unicode__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return 'room/{}/'.format(self.id)

    class Meta:
        db_table = 'rooms'


class Reservation(models.Model):
    TIMES = [
        ("08:00-08:30", "08:00-08:30"),
        ("08:30-09:00", "08:30-09:00"),
        ("09:00-09:30", "09:00-09:30"),
        ("09:30-10:00", "09:30-10:00"),
        ("10:00-10:30", "10:00-10:30"),
        ("10:30-11:00", "10:30-11:00"),
        ("11:00-11:30", "11:00-11:30"),
        ("11:30-12:00", "11:30-12:00"),
        ("12:00-12:30", "12:00-12:30"),
        ("12:30-13:00", "12:30-13:00"),
        ("13:00-13:30", "13:00-13:30"),
        ("13:30-14:00", "13:30-14:00"),
        ("14:00-14:30", "14:00-14:30"),
        ("14:30-15:00", "14:30-15:00"),
        ("15:00-15:30", "15:00-15:30"),
        ("15:30-16:00", "15:30-16:00"),
        ("16:00-16:30", "16:00-16:30"),
        ("16:30-17:00", "16:30-17:00"),
        ("17:00-17:30", "17:00-17:30"),
        ("17:30-18:00", "17:30-18:00"),
        ("18:00-18:30", "18:00-18:30"),
        ("18:30-19:00", "18:30-19:00")
    ]

    login = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    date = models.DateField()
    time = models.CharField(max_length=15, choices=TIMES)

    note = models.CharField(max_length=100)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return '{}:{}-{}-{}-{}'.format(self.login, self.room.name, self.date, self.time, self.is_blocked, self.note)

    def __unicode__(self):
        return '{}:{}-{}-{}-{}'.format(self.login, self.room.name, self.date, self.time, self.is_blocked, self.note)

    def get_absolute_url(self):
        return 'reservation/{}/'.format(self.id)

    class Meta:
        db_table = 'reservation'


class Administrator(models.Model):
    login = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.login)

    def __unicode__(self):
        return '{}'.format(self.login)

    # def get_absolute_url(self):
    #     return 'administrator/{}/'.format(self.id)

    class Meta:
        db_table = 'administrator'
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
    login = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    date = models.DateField()
    time = models.CharField(max_length=100)

    note = models.CharField(max_length=100)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return '{}:{}-{}-{}-{}'.format(self.login, self.room.name, self.date, self.start_time, self.end_time)

    def __unicode__(self):
        return '{}:{}-{}-{}-{}'.format(self.login, self.room.name, self.date, self.start_time, self.end_time)

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
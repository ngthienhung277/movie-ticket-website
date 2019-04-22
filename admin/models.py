from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255)
    summary = models.TextField()
    birthdate = models.DateField()
    nationality = models.CharField(max_length=255)
    bio = models.TextField()
    # TODO: Pictures


class Actor(models.Model):
    name = models.CharField(max_length=255)
    summary = models.TextField()
    birthdate = models.DateField()
    nationality = models.CharField(max_length=255)
    bio = models.TextField()
    # TODO: Pictures


class Genre(models.Model):
    name = models.CharField(max_length=40)


class Movie(models.Model):
    name = models.CharField(max_length=255)
    running_time = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=255)
    directors = models.ManyToManyField(Director)
    actors = models.ManyToManyField(Actor)
    genre = models.ManyToManyField(Genre)
    production_company = models.CharField(max_length=255)
    release_date = models.DateField()
    content = models.TextField()
    # TODO: Trailer and Picture


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    phone = models.CharField(max_length=10, min_length=10)
    number_screening_room = models.PositiveSmallIntegerField()
    number_seats = models.PositiveSmallIntegerField()
    # TODO: Status of cinema?

class ScreeningRoom(models.Model):
    # TODO: Combined unique constraints
    room_number = models.PositiveSmallIntegerField()
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    # TODO: status
    number_seats = models.PositiveSmallIntegerField()
    number_rows = models.PositiveSmallIntegerField()


class Seat(models.Model):
    seat_number = models.PositiveSmallIntegerField()
    seat_row = models.CharField(max_length=1)
    screening_room = models.ForeignKey(ScreeningRoom, on_delete=models.CASCADE)


class MovieSchedule(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    screening_room = models.ForeignKey(ScreeningRoom, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

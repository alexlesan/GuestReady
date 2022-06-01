import imp
from django.db import models
from django.utils.text import slugify
from django.db.models import Subquery, OuterRef


class Rental(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name, allow_unicode=True)
        return super(Rental, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name ="Rental"
        verbose_name_plural = "Rentals"

class ReservationQuerySet(models.QuerySet):

    def collect(self):
        subquery = self.filter(rental=OuterRef("rental"), checkin__lt=OuterRef("checkin")).exclude(id=OuterRef('id')).order_by("-checkin")
        return self.annotate(prev_id=Subquery(subquery.values('id')[:1])).order_by('rental__name', 'checkin')

class ReservationManager(models.Manager):

    def get_queryset(self):
        return ReservationQuerySet(self.model, using=self._db)

    def collect(self):
        return self.get_queryset().collect()

class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    checkin = models.DateField()
    checkout = models.DateField()

    objects= ReservationManager()

    def __str__(self) -> str:
        return f"{self.title}({self.checkin} - {self.checkout})"

    class Meta: 
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"


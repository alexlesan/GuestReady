from django.db import models
from django.utils.text import slugify


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



class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    checkin = models.DateField()
    checkout = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.title}({self.checkin} - {self.checkout})"

    class Meta: 
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"


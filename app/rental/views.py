import imp
from django.db.models import OuterRef, Subquery
from django.shortcuts import render
from django.views import View
from .models import Reservation


class ReservationView(View):
    template = 'rental/reservation_list.html'

    def get(self, request):
        res = Reservation.objects.filter(rental=OuterRef("rental"), checkin__lt=OuterRef("checkin")).exclude(id=OuterRef('id')).order_by("-checkin")
        reservations = Reservation.objects.all().annotate(prev_id=Subquery(res.values('id')[:1])).order_by('rental__name', 'checkin')
        return render(request, self.template, {'reservations': reservations})
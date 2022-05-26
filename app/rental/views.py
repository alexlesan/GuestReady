import imp
from django.shortcuts import render
from django.views import View
from .models import Reservation


class ReservationView(View):
    template = 'rental/reservation_list.html'

    def get(self, request):
        reservations = Reservation.objects.all().order_by('rental__name', 'checkin')
        for reservation in reservations:
            prev = reservations.filter(checkin__lt=reservation.checkin, rental=reservation.rental).exclude(id=reservation.id).order_by('-checkin').first()
            if prev:
                reservation.prev_id = prev.id
            else:
                reservation.prev_id = '---'

        return render(request, self.template, {'reservations': reservations})

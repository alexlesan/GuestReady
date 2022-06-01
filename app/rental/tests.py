import imp
from unicodedata import name
from urllib import response
from django.test import TestCase
from .models import Rental, Reservation

class RentalTestCase(TestCase):
    def setUp(self) -> None:
        Rental.objects.create(name="Rental-1", slug='rental-1')
        Rental.objects.create(name="Rental-2", slug='rental-2')

    def test_rental_created(self):
        rental_1 = Rental.objects.get(name='Rental-1')
        rental_2 = Rental.objects.get(name='Rental-2')

        self.assertEqual(rental_1.name, 'Rental-1')
        self.assertEqual(rental_2.name, 'Rental-2')

    def test_column_name_label(self):
        rental_1 = Rental.objects.get(name='Rental-1')
        column_name_label = rental_1._meta.get_field('name').verbose_name
        self.assertEqual(column_name_label, 'name')


    def test_column_slug_label(self):
        rental_1 = Rental.objects.get(name='Rental-1')
        column_slug_label = rental_1._meta.get_field('slug').verbose_name
        self.assertEqual(column_slug_label, 'slug')

    def test_slug_value(self):
        rental_1 = Rental.objects.get(name='Rental-1')
        slug_rental_1 = 'rental-1'
        
        self.assertEqual(rental_1.slug, slug_rental_1)


class ReservationTestCase(TestCase):
    def setUp(self):
        rental = Rental.objects.create(name='Rental-test')
        Reservation.objects.create(rental=rental, title="Reservation-1", checkin='2022-01-01', checkout='2022-01-13')
        Reservation.objects.create(rental=rental, title="Reservation-2", checkin='2022-01-20', checkout='2022-02-10')

    def test_column_title_label(self):
        res = Reservation.objects.get(title='Reservation-1')
        column_title = res._meta.get_field('title').verbose_name
        self.assertEqual(column_title, 'title')

    def test_column_checkin_label(self):
        res = Reservation.objects.get(title='Reservation-1')
        column_checkin = res._meta.get_field('checkin').verbose_name
        self.assertEqual(column_checkin, 'checkin')

    def test_column_checkout_label(self):
        res = Reservation.objects.get(title='Reservation-1')
        column_checkout = res._meta.get_field('checkout').verbose_name
        self.assertEqual(column_checkout, 'checkout')

    def test_reservation_without_prev_res_id(self):
        res = Reservation.objects.collect().get(title='Reservation-1')
        self.assertEqual(res.prev_id, None)

    def test_reservation_with_prev_res_id(self):
        res = Reservation.objects.collect().get(title="Reservation-2")
        self.assertNotEqual(res.prev_id, None)


class UrlsTestCase(TestCase):
    def test_view_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
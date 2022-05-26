# Generated by Django 4.0.4 on 2022-05-25 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
            ],
            options={
                'verbose_name': 'Rental',
                'verbose_name_plural': 'Rentals',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateField()),
                ('checkout', models.DateField(blank=True, null=True)),
                ('rental', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.rental')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
        ),
    ]
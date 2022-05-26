# Django app using Docker + nginx

Requirements:
    - Docker installed

# How to start
    - from the root folder run the command 'docker-compose -f docker-compose-deploy.yml up --build'
    - Run tests, run the command in terminal 'docker-compose run --rm app sh -c "python manage.py test"


# GuestReady
GuestReady rental test
Lets we have a django project.
With models:
#
```
Rental
 - name

Reservation
  -rental_id
  -checkin(date)
  -checkout(date)


Add the view with the table of Reservations with "previous reservation ID".
Previous reservation is a reservation that is before the current one into same
rental.


Example:
Rental-1
Res-1(2022-01-01, 2022-01-13)
Res-2(2022-01-20, 20fro22-02-10)
Res-3(2022-02-20, 2022-03-10)

Rental-2
Res-4(2022-01-02, 2022-01-20)
Res-5(2022-01-20, 2022-02-11)


|Rental_name|ID      |Checkin    |Checkout  |Previous reservation, ID|
|rental-1   |Res-1 ID| 2022-01-01|2022-01-13| -                      |
|rental-1   |Res-2 ID| 2022-01-20|2022-02-10| Res-1 ID               |
|rental-1   |Res-3 ID| 2022-02-20|2022-03-10| Res-2 ID               |
|rental-2   |Res-4 ID| 2022-01-02|2022-01-20| -                      |
|rental-2   |Res-5 ID| 2022-01-20|2022-01-11| Res-4 ID               |
```
#

# Result preview
![alt text](https://github.com/alexlesan/GuestReady/blob/main/Reservations.png?raw=true)
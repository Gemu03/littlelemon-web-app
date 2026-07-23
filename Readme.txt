=========================================================
      LITTLE LEMON RESTAURANT WEB APPLICATION CAPSTONE
=========================================================

Welcome to the Little Lemon REST API and web application, built using Django and Django REST Framework.

---------------------------------------------------------
1. API ENDPOINTS FOR PEER REVIEW
---------------------------------------------------------

Here are the paths you can test using Insomnia or Postman:

* User Registration (POST):
  /api/users/

* Token Login / Authentication (POST):
  /api/token/login/

* Menu Items List & Creation (GET/POST):
  /api/menu-items/

* Single Menu Item details (GET/PUT/PATCH/DELETE):
  /api/menu-items/<id>/

* Table Booking List & Creation (GET/POST):
  /api/booking/tables/

* Table Booking Alternative Path (GET/POST):
  /api/bookings/

* Single Booking details (GET/PUT/PATCH/DELETE):
  /api/bookings/<id>/

---------------------------------------------------------
2. TEST USER CREDENTIALS
---------------------------------------------------------

A pre-populated superuser account has been created in the database for immediate testing:
- Username: admin
- Password: adminpass

---------------------------------------------------------
3. PROJECT VERIFICATION STEPS
---------------------------------------------------------

To run this project locally, execute the following steps:

1. Install dependencies:
   $ pipenv install
   $ pipenv shell

2. Apply migrations:
   $ python manage.py migrate

3. Run the unit tests:
   $ python manage.py test

4. Run the development server:
   $ python manage.py runserver

Once the server is running, the responsive HTML home page will be served at http://127.0.0.1:8000/.

=========================================================
        Thank you for reviewing my project!
=========================================================

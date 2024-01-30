#!/usr/bin/bash


# shellcheck disable=SC2164
#cd cafe_dr

./manage.py migrate  && gunicorn -b 0.0.0.0:8080 cafe_dr.wsgi:application
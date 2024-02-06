FROM python:3.10

RUN mkdir "/Cafe_app"

WORKDIR /Cafe_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

WORKDIR cafe_dr

CMD python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root', 'root@example.com', 'root')" \
    && gunicorn cafe_dr.wsgi:application --bind 0.0.0.0:8080 --log-level info

FROM python:3.9

ADD requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /yutvdom_django

CMD python manage.py runserver 0.0.0.0:8000
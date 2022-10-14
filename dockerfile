FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /oc_lettings_site

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
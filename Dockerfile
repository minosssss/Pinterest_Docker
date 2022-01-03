FROM python:3.8.0

WORKDIR /home/

RUN git clone https://github.com/minosssss/Pinterest_Docker.git

WORKDIR /home/Pinterest_Docker/

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=%01tw4o1wkl#p@0h#bc(@9j8r*2qu3lg^l@n1ety%5olgmlcw" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]
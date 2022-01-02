FROM python:3.8.0

WORKDIR /home/

RUN git clone https://github.com/minosssss/Pinterest_Docker.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=%01tw4o1wkl#p@0h#bc(@9j8r*2qu3lg^l@n1ety%5olgmlcw" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
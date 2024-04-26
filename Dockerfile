FROM django:onbuild
FROM python:3.12

ENV PYTHONBUFFERED=1

WORKDIR /DJANGO-LEARNWITHUS

COPY  requirements.txt .

RUN  pip install -r requirements.txt

COPY . .

EXPOSE 8000
EXPOSE 80

CMD [ "python","manage.py","runserver"]
FROM python

RUN mkdir /app
WORKDIR /app
COPY ./ /app/

RUN pip install -r /app/requirements.txt

RUN python manage.py db init
RUN python manage.py db migrate
RUN python manage.py db upgrade

EXPOSE 5000

CMD python manage.py run





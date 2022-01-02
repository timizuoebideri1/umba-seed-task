FROM python

RUN mkdir /app
WORKDIR /app
COPY ./ /app/

RUN pip install -r /app/requirements.txt

EXPOSE 5000

CMD python manage.py run





FROM python

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000/tcp

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app

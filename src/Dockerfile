FROM python

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

COPY . .

EXPOSE 8000/tcp

# Run the application with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
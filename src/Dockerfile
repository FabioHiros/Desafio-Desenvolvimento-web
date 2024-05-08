FROM python

workdir /src

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ..

EXPOSE 5000/tcp

CMD ['python','-m','flask','run','--host-0.0.0.0']
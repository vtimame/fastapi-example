FROM python:3.10.2

ADD . /srv/app
WORKDIR /srv/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]
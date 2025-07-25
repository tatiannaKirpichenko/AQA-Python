FROM python:3-slim

RUN apt-get update && apt-get install -y libffi-dev gcc

WORKDIR /app

COPY requirements.txt /app/
RUN pip install  -r requirements.txt

COPY . /app/

EXPOSE 7000

CMD ["gunicorn", "-b", "0.0.0.0:7000", "wsgi:app"]


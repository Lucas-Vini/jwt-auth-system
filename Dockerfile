FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
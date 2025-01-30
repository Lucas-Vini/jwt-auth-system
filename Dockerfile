FROM python:3.12-slim

WORKDIR /

COPY requirements.txt /

RUN pip install --no-cache-dir -r requirements.txt

COPY . /

EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "app.__main__:app"]
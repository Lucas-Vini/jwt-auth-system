FROM python:3.12-slim

WORKDIR /

COPY requirements.txt /

RUN pip install --no-cache-dir -r requirements.txt

COPY . /

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 80

CMD if [ "$FLASK_ENV" = "development" ]; \
    then flask run -p 80 --debug; \
    else gunicorn -b 0.0.0.0:80 app.__main__:app; \
    fi
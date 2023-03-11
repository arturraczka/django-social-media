FROM python:3.10.6
ENV PYTHONBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app
COPY Pipfile Pipfile.lock /app/
RUN pip install --upgrade pip setuptools pipenv
RUN pipenv install --deploy --system --dev
COPY . /app
WORKDIR /app/headlet
CMD python manage.py runserver 0.0.0.0:8000

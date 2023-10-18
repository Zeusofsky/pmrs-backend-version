# Track and Trace Project

A web application using Django REST framework is a service of track and trace articles and shipments.

The Track and Trace app provides API for getting information about articles and shipments along with corresponding weather information. 

This app has the following features:

- users can create/read/update/delete customers via rest api
- users can create/read/update/delete shops via rest api
- users can create/read/update/delete shipments via rest api
- for getting actual weather data the Weather app uses OpenWeather api service https://openweathermap.org/api
- users can retrieve weather information from OenWeatherMap by zip code and country code via rest api
- users can retrieve weather information from OenWeatherMap by customer id via rest api
- users can retrieve weather information from OenWeatherMap by zip code and country code trough celery async task via rest api


The application has been covered with unit tests.

____
## Requirements

- Python 3.7+
- Django 3.1

## Packages

- django
- django-rest-framework
- django-cors-headers 
- python-decouple
- drf-spectacular (Open API)
- celery
- redis

## Installing

1\. Clone the repository:
```
git clone https://github.com/AliSajadian/track_and_trace_api.git
```
2\. install requirements:
```
pip install -r requirements.txt
```
3\. create Postgresql database and user:
```

```
4\. migrate to database
```
python manage.py makemigrations
python manage.py migrate
```

## Usage

before use async weather endpoint call create a worker as following:
```
celery -A main worker -l info
```
or
```
celery -A main worker -l info --logfile=celery.log --detach
```


# temp_chart
## Introduction
A Django application that takes in temperature and city_name readings over time, stores them in a database and shows the data on a timeseries chart.


 The features include;
 
 1. As a user I can fill in the form by city_name and temperature
 2. As a user I can view the temperature data in a line graph
 3. plot charts from models, i.e, lin chart and pie chart
 4. plot data from models on the same axis

 

 # Dependencies
 The app depends on multiple packages;

   1.**Django Framework**- A web framework for Python. 
 
   3.**Django-chartit** - Django Chartit is a Django app that can be used to easily create charts from the  data in your database. The charts are rendered using Highcharts and jQuery JavaScript libraries.
  
# Installation and Setup

**To be able to get this project to your local machine**


```sh
$ git clone https://github.com/BethMwangi/temp_chart.git
$  pip install virtual env
$ . venv/bin/activate
$  cd django_app/
$ pip install -r requirements.txt



 ## To execute the demo run the commands

 ```sh
$ PYTHONPATH=../ python ./manage.py migrate
$ PYTHONPATH=../ python ./manage.py runserver


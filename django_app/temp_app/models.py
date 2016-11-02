from __future__ import unicode_literals
import datetime
from django.db import models


class TempChart(models.Model):
	city_name = models.CharField(max_length=40)
	temperature = models.IntegerField()
	date = models.DateTimeField(default=datetime.datetime.now)

	# def __unicode__(self):
	# 	return self.temperature

from __future__ import unicode_literals
import datetime
from django.db import models

from django.utils import timezone


class TempChart(models.Model):
	temperature = models.IntegerField()
	created_date = models.DateTimeField(default=timezone.now)


	class Meta:
		db_table = "tempchart"

	def __repr__(self):
		return '<%r, %r>' % (self.temperature, self.created_date)





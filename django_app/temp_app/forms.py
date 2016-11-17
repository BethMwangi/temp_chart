from django import forms
from temp_app.models import TempChart
from views import *


class TempChartForm(forms.Form):
	"""docstring for TempForm"""

	temperature = forms.IntegerField()
	

	
	
		
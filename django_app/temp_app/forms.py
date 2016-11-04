from django import forms
from models import TempChart


class TempChartForm(forms.Form):
	"""docstring for TempForm"""

	city_name = forms.CharField(max_length=50)
	temperature = forms.IntegerField()
	

	
	
		
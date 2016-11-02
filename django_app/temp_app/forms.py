from django import forms
from models import TempChart


class TempForm(forms.Form):
	"""docstring for TempForm"""

	city_name = forms.CharField()
	temperature = forms.IntegerField()
	date = forms.DateTimeField()

	
	
		
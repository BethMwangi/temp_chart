from django.shortcuts import render, render_to_response
from django.http import HttpResponse,  HttpResponseRedirect
from temp_app.forms import TempForm
from temp_app.models import TempChart
from django.views.decorators.csrf import csrf_protect
import datetime
from django import forms
from django.utils import timezone

def main_page(request):

	if request.method == 'POST':
		form = TempForm(request.POST or None)
		if form.is_valid():
			temp.city_name = form.cleaned_data['city_name']
			temp.temperature = form.cleaned_data['temperature']
			temp.save()

			return HttpResponseRedirect('list_temp')
	else:
		form = TempForm()


	return render(request, 'create.html', {'form': form
			})


def list_temp(request):
	temperatures = TempChart.objects.all()
	return render_to_response('list_temp.html', {'temperatures': temperatures})


















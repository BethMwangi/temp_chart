from django.shortcuts import render, render_to_response
from django.http import HttpResponse,  HttpResponseRedirect
from temp_app.forms import TempForm
from temp_app.models import TempChart
from django.views.decorators.csrf import csrf_protect
import datetime
from django import forms
from django.utils import timezone
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from chartit import DataPool, Chart



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


# def list_temp(request):
# 	temperatures = TempChart.objects.all()
# 	return render_to_response('list_temp.html', {'temperatures': temperatures})
# 	# return HttpResponse(json.dumps(data))


def list_temp(request):
	# crete a datapool with the data we want to retrieve
	tempdata = DataPool(
		series= [{'options': {
		'source':TempChart.objects.all()},
		'terms': [
		'city_name',
		'temperature',
		'created_date']}
		])
	
	# create chart object

	cht = Chart(
		datasource = tempdata,
		series_options = 
		[{'options':{
		'type': 'line',
		'stacking': False},
		'terms':{
		'city_name': [
		'temperature',
		'created_date']
		}}],
		chart_options = 
		{'title': {
		'text': 'Temp Data by City_name'},
		'xAxis': {
		'title' : {
		'text': 'City_name'}}})


	# Send the chart object to the template.
	# return render_to_response({'list_temp': cht})
	return render_to_response('list_temp.html', {'tempchart':cht})






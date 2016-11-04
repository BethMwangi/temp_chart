from django.shortcuts import render, render_to_response
from django.http import HttpResponse,  HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from random import randint
from temp_app.forms import TempChartForm
from temp_app.models import TempChart
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from chartit import DataPool, Chart



def main_page(request):
	if request.method == 'POST':
		form = TempChartForm(request.POST)
		if form.is_valid():
			request.session['text'] = form.cleaned_data['city_name']
			# temp = form.save(commit=False)
			# temp.city_name = form.cleaned_data['city_name']
			# temp.temperature = form.cleaned_data['temperature']
			# temp = TempChart(city_name=city_name, temperature=temperature)
			
			# temp.save()
			
			return HttpResponseRedirect('/list_temp') #redirect after POST
	else:
		form = TempChartForm()
	return render(request, 'main_page.html', {'form': form
			})




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
		'temperature']
		}}],
		chart_options = 
		{'title': {
		'text': 'Temp Data by City_name'},
		'xAxis': {
		'title' : {
		'text': 'City_name'}}})


	# Send the chart object to the template.

	return render_to_response('list_temp.html', {'tempchart':cht})






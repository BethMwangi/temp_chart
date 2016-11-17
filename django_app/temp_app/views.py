from django.shortcuts import render, render_to_response
from django.http import HttpResponse,  HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from random import randint
# from forms import TempChartForm
# from models import TempChart
from temp_app.models import TempChart
from temp_app.forms import TempChartForm
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from chartit import DataPool, Chart



def main_page(request):
	form = TempChartForm
	if request.POST:
		form = TempChartForm(request.POST)
		if form.is_valid():
			temp = form.save(commit=False)
			temp.save()
			return redirect( 'list_temp.html')
	
	return render(request, 'main_page.html', {'form': form
			})




def list_temp(request):
	# crete a datapool with the data we want to retrieve
	tempdata = DataPool(
		series= [{'options': {
		'source':TempChart.objects.all()},
		'terms': [
		'temperature',
		'created_date']}
		])
	
	# create chart object

	cht_1 = Chart(
		datasource = tempdata,
		series_options = 
		[{'options':{
		'type': 'line',
		'stacking': False},
		'terms':{
		'created_date': [
		'temperature']
		}}],
		chart_options = 
		{'title': {
		'text': 'Temp Data by Time'},
		'xAxis': {
		'title' : {
		'text': 'Data'}}})


	# crete a datapool with the data we want to retrieve to create a pie chart
	ds = DataPool(
		series= [{'options': {
		'source':TempChart.objects.all()},
		'terms': [
		'temperature',
		'created_date']}
		])

	def cityname(city_num):
		created_date = {1: '', 2: '', 3: '', 4: '', 5: ''}
		return names[city_num]


	cht_2 = Chart(
		datasource = ds,
		series_options = 
		[{'options':{
		'type': 'pie',
		'stacking': False},
		'terms':{
		'created_date': [
		'temperature']
		}}],
		chart_options = 
		{'title': {
		'text': 'Temp Data by Time'},
		'title' : {
		'text': 'created_date'}})


	# Send the chart object to the template.

	return render_to_response('list_temp.html', {'tempchart': [cht_1, cht_2], })






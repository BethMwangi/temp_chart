from django.shortcuts import render, render_to_response
from django.http import HttpResponse,  HttpResponseRedirect
from temp_app.forms import TempForm
from temp_app.models import TempChart
from django.views.decorators.csrf import csrf_protect
import datetime

def main_page(request):
	form = TempForm()
	if request.method == 'POST':
		form = TempForm(request.POST or None)
		if form.is_valid():
			city_name = request.POST.get('city_name', '')
			temperature = request.POST.get('temperature', '')
			date = request.POST.get('date', '')
			form = TempChart( city_name=city_name, temperature=temperature, date=date)
			form.save()

			return HttpResponseRedirect('temperatures')
		# else:
		# 	form = TempForm()
			# args = {}
			# args.update(csrf(request))

			# args['form'] = form
	return render(request, 'create.html', {'form': form
			})






# 	output = '''
# 	<html><head><title>%s</title></head>
# 	<body>
# 	<h1> %s</h1><p>%s</p>
# 	</body>
# 	</html>
# 	''' % (
# 		'First Project',
# 		'I hope it works out perfectly',
# 		'learning....10%')

# 	return HttpResponse(output)

# def create(request):
# 	form = TempForm()
# 	if request.method == 'POST':
# 		form = TempForm(request.POST or None)
# 		if form.is_valid():
# 			city_name = request.POST.get('city_name', '')
# 			temperature = request.POST.get('temperature', '')
# 			date = request.POST.get('date', '')
# 			form = TempChart( city_name=city_name, temperature=temperature, date=date)
# 			form.save()

# 			return HttpResponseRedirect('temperatures')
# 		# else:
# 		# 	form = TempForm()
# 			# args = {}
# 			# args.update(csrf(request))

# 			# args['form'] = form
# 	return render_to_response(request, 'create.html', {'form': form
# 			})
# 		# return render(request, 'create_temp.html' , {'form': form
# 		# 	})













from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
	output = '''
	<html><head><title>%s</title></head>
	<body>
	<h1> %s</h1><p>%s</p>
	</body>
	</html>
	''' % (
		'First Project',
		'I hope it works out perfectly',
		'learning....10%')

	return HttpResponse(output)

# Create your views here.
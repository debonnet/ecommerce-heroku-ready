from django.shortcuts import render

# Create your views here.
def search(request):

	template = 'test/test.html'
	context = {}
	return render(request, template, context)
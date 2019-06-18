from django.shortcuts import render

# Create your views here.
def home_view(request):
	return render(request,'home.html')

def design(request):
	return render(request,'design.html')

def form2(request):
    	return render(request, 'form2.html')


def form1(request):
    	return render(request, 'form1.html')

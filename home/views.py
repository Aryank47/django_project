from django.shortcuts import render
from home.forms import customForms
from home.forms import library

# Create your views here.
def home_view(request):
	return render(request,'home.html')

def design(request):
	return render(request,'design.html')

def form2(request):
    	return render(request, 'form2.html')


def form1(request):
    	return render(request, 'form1.html')


def carousel(request):
    	return render(request, 'carousel.html')


def form_view(request):
    msg = ''
    if request.method == 'POST':
        form = customForms(request.POST)
        if form.is_valid():
            lib = library.objects.create(
                Studentname=form.cleaned_data.get('Studentname'),
                Branch=form.cleaned_data.get('Branch'),
                IssueDate=form.cleaned_data.get('IssueDate'),
                SubmissionDate=form.cleaned_data.get('SubmissionDate'),
                IssuedBooks=form.cleaned_data.get('IssuedBooks')
            )
            lib.save()
            msg = 'Data added to library'

        else:
            msg = form.errors
    else:
        form = customForms()
    return render(request, 'forms.html', {"msg": msg, "forms": form, })

    #  lib=library(
    #     Studentname=form.cleaned_data.get('Studentname'),
    #     Branch=form.cleaned_data.get('Branch'),
    #     IssueDate=form.cleaned_data.get('IssueDate'),
    #     SubmissionDate=form.cleaned_data.get('SubmissionDate'),
    #     IssuedBooks=form.cleaned_data.get('IssuedBooks')
    # )

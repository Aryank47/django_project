from django import forms
from home.models import library
from datetime import date


class customForms(forms.Form):
    Studentname = forms.CharField(label='Name',
                                  widget=forms.TextInput(
                                      attrs={'maxlength': '30', 'placeholder': 'StudentName', 'class': 'form-control'}))
    Branch = forms.CharField(label='Branch', widget=forms.TextInput(
        attrs={'maxlength': '20', 'placeholder': 'Branch', 'class': 'form-control'}))
    IssueDate = forms.DateField(label='IssueDate', widget=forms.DateInput(
                                attrs={'maxlength': '30', 'placeholder': 'Issuedate', 'class': 'form-control'}))
    SubmissionDate = forms.DateField(label='SubmissionDate', widget=forms.DateInput(
        attrs={'maxlength': '30', 'placeholder': 'SubmissionDate', 'class': 'form-control'}))
    IssuedBooks = forms.IntegerField(label='BooksIssued', widget=forms.NumberInput(
        attrs={'maxlength': '30', 'placeholder': 'BooksIssued', 'class': 'form-control'}))


# class ModelcustomForms(forms.Form):
#     Studentname=forms.CharField(label='Name',
#                             widget=forms.TextInput(
#                                 attrs={'maxlength':'30','placeholder':'StudentName','class':'form-control'}))
#     Branch=forms.CharField(label='Branch',widget=forms.TextInput(attrs={'maxlength':'20','placeholder':'Branch','class':'form-control'}))
#     IssueDate=forms.DateField(label='IssueDate',widget=forms.DateInput(
#                                 attrs={'maxlength':'30','placeholder':'Issuedate','class':'form-control'}))
#     SubmissionDate=forms.DateField(label='SubmissionDate',widget=forms.DateInput(
#                                 attrs={'maxlength':'30','placeholder':'SubmissionDate','class':'form-control'}))
#     IssuedBooks=forms.IntegerField(label='BooksIssued',widget=forms.NumberInput(
#                                 attrs={'maxlength':'30','placeholder':'BooksIssued','class':'form-control'}))
#     class Meta:
#         model=library
#         fields='__all__'

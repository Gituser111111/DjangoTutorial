from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request, 'FE_test/index.html', {})



def aboutUs(request):
	pass

def knowledge(request):
	pass

def login(requets):
	pass

def member_detail(requet):
	pass

def member_invest(request):
	pass

def register(request):
	pass
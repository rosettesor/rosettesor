from django.shortcuts import render

# Create your views here.
def index(request):
    return renter(request, 'spermies.html')

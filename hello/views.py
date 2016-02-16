from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'spermies.html')

def nfl_rainbow(request):
    return render(request, 'nfl_rainbow.html')

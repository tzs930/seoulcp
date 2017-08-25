from django.shortcuts import render
from django.utils import timezone

def main(request):
    return render(request, 'main/main.html', {})

# Create your views here.

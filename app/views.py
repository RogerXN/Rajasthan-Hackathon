from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def sign(request):
    return render(request, 'signin.html')

def About(request):
    return render(request, 'About.html')
def School(request):
    return render(request, 'school.html')

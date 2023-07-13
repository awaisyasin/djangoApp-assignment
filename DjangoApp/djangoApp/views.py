from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'djangoApp/index.html')

def detail(request):
    return render(request, 'djangoApp/detail.html')

def header(request):
    return render(request, 'djangoApp/header.html')

def footer(request):
    return render(request, 'djangoApp/footer.html')
from django.shortcuts import render

# Create your views here.
def index(request): #Top page
    return render(request, 'pages/index.html')
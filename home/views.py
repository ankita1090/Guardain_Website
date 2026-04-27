from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')
def documentation(request):
    return render(request, 'documentation.html')
def about(request):
    return HttpResponse("hey this is about page")
def service(request):
    return HttpResponse("hey this is service page")

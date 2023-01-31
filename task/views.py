from django.shortcuts import render, HttpResponse

# Create your views here.
def tasksList(request):
    return render(request, 'lista.html')
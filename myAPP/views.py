from django.shortcuts import render
from django.http import HttpResponse

def showform(request):
    return render(request, "form.html")

def getform(request):
    if request.method == 'POST':
        name = request.POST['name']
        id = request.POST['id']
        # Return the form data in HTTP response
        return HttpResponse("Name: " + name + ", UserID: " + id)
    else:
        return HttpResponse("Invalid request method")


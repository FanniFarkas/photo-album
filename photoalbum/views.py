from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello World! I'm Home. I am Fanni.")

def about(request):
    return HttpResponse("My About page.")
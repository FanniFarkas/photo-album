from django.shortcuts import render
from .models import Photo



def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photos.html', {'photos' : photos})

def picture_page(request, name):
    photo = Photo.objects.get(title = name)
    return render(request, 'picture.html', {'photo' : photo})
from django.shortcuts import render
from .models import Photo
from django.contrib.auth.decorators import login_required


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photos.html', {'photos' : photos})

def picture_page(request, name):
    photo = Photo.objects.get(title = name)
    return render(request, 'picture.html', {'photo' : photo})

def picture_page(request, name):
    photo = Photo.objects.get(title = name)
    return render(request, 'picture.html', {'photo' : photo})

@login_required(login_url="/users/login")
def new_photo_page(request):
    return render(request, 'new_photo.html')
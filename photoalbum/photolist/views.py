from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from django.contrib.auth.decorators import login_required
from . import forms

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
    if request.method == 'POST':
        form = forms.CreatePhoto(request.POST, request.FILES)
        if form.is_valid():
            newphoto=form.save(commit=False)
            newphoto.owner = request.user
            newphoto.save()
            return redirect('photos:list')
    else:
        form = forms.CreatePhoto()
    return render(request, 'new_photo.html', {'form': form})

@login_required(login_url="/users/login")
def delete_photo(request, name):
    photo = get_object_or_404(Photo, title=name)
    
    if photo.owner == request.user:
        photo.delete()
    
    return redirect('photos:list')


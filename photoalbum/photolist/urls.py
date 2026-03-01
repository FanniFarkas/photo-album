from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.photo_list, name = "list"),
    path('new_photo/', views.new_photo_page, name = "new"),
    path('<slug:name>/', views.picture_page, name = "picture"),
]
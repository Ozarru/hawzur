from django.urls import path

from . import views

urlpatterns = [
    # video urls----------------------------------------------------------------
    path('upload/', views.uploadVideo, name='upload-video'),
    path('display/<int:id>/', views.displayVideo, name='display-video'),
    # path('update-video/<int:id>/', views.updateVideo, name='update-video'),
    # path('delete-video/<int:id>/', views.deleteVideo, name='delete-video'),

]

from django.urls import path

from . import views

urlpatterns = [
    # auth urls----------------------------------------------------------------
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    # home url=----------------------------------------------------------------
    path('', views.home, name='home'),

    # room urls----------------------------------------------------------------
    path('create-room/', views.createRoom, name='create-room'),
    path('room/<int:id>/', views.room, name='room'),
    path('update-room/<int:id>/', views.updateRoom, name='update-room'),
    path('delete-room/<int:id>/', views.deleteRoom, name='delete-room'),

    # message urls-------------------------------------------------------------
    # path('update-message/<int:id>/', views.updateMessage, name='update-message'),
    path('delete-message/<int:id>/', views.deleteMessage, name='delete-message'),

    # user profile urls--------------------------------------------------------
    path('profile/<int:id>/', views.userProfile, name='user-profile'),
    path('update-user/', views.updateUser, name='update-user'),

]

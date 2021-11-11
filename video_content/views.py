from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from video_content.forms import VideoForm
from video_content.models import Video
from django.contrib.auth.decorators import login_required

# import video_content

# Create your views here.

# video reading page------------------------------------------------------------------------------------


def uploadVideo(request):

    if request.method == 'POST':

        title = request.POST['title']
        video = request.POST['video']

        content = Video(title=title, video=video)
        content.save()
        return redirect('home')

    return render(request, 'video_form.html')


def displayVideo(request):

    videos = Video.objects.all()
    context = {
        'videos': videos,
    }

    return render(request, 'videos.html', context)

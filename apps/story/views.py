import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StoryForm
from .models import Story
# Create your views here.
def frontpage(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days =1)
   ## stories = Story.objects.filter(created_at__gte=date_from).order_by('-number_of_votes')[0:30]
    stories = Story.objects.all().order_by('-number_of_votes')[0:30]


    return render(request, 'story/frontpage.html',{'stories':stories})

@login_required
def submit(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.created_by = request.user
            story.save()
            
            return redirect('frontpage')
    form = StoryForm()
    
    return render(request, 'story/submit.html',{'form': form})
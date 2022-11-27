import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SubmissionForm
from .models import Submission
# Create your views here.
def frontpage(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days =1)
    ##submissions = Submission.objects.filter(created_at__gte=date_from).order_by('-number_of_votes')[0:30]
    submissions = Submission.objects.all().order_by('-number_of_votes')[0:30]


    return render(request, 'submission/frontpage.html',{'submissions':submissions})

def newest(request):
    submissions = Submission.objects.all()[0:200]
    return render(request, 'submission/newest.html', {'submissions':submissions})

@login_required
def submit(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.created_by = request.user
            submission.save()
            
            return redirect('frontpage')
    form = SubmissionForm()
    
    return render(request, 'submission/submit.html',{'form': form})
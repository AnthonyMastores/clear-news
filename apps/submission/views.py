import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SubmissionForm, CommentForm
from .models import Submission, Vote, Comment
# Create your views here.
def frontpage(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days =1)
    submissions = Submission.objects.all().order_by('-number_of_votes')[0:30]


    return render(request, 'submission/frontpage.html',{'submissions':submissions})

def newest(request):
    submissions = Submission.objects.all()[0:200]
    return render(request, 'submission/newest.html', {'submissions':submissions})

@login_required
def comment(request, submission_id):
    submission = get_object_or_404(Submission,pk=submission_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.submission = submission
            comment.created_by = request.user
            comment.save()
            
            return redirect('comment',submission_id=submission_id)
    else:
        form = CommentForm()
        
    return render(request, 'submission/detail.html', {'submission': submission, 'form': form})
    
@login_required
def vote(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    if submission.created_by != request.user and not Vote.objects.filter(created_by=request.user, submission=submission):
        vote = Vote.objects.create(submission=submission, created_by=request.user)
    
    return redirect('frontpage')

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


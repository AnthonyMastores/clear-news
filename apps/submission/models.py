from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Submission(models.Model):
    title = models.CharField(max_length = 255)
    url = models.URLField()
    number_of_votes = models.IntegerField(default=1)
    created_by = models.ForeignKey(User, related_name='submissions',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return '%s' % self.title
    
class Vote(models.Model):
    submission = models.ForeignKey(Submission, related_name='votes', on_delete=models.CASCADE)

    created_by = models.ForeignKey(User, related_name='votes', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.submission.number_of_votes = self.submission.number_of_votes + 1
        self.submission.save()

        super(Vote, self).save(*args, **kwargs)
        
class Comment(models.Model):
    submission = models.ForeignKey(Submission, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    
    created_by = models.ForeignKey(User, related_name='comments',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
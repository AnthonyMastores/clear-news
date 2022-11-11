from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Story(models.Model):
    title = models.CharField(max_length = 255)
    url = models.URLField()
    number_of_votes = models.IntegerField(default=1)
    created_by = models.ForeignKey(User, related_name='stories',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return '%s' % self.title
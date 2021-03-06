from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=1250)

    def __str__(self):
        return self.title
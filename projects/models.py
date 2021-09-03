from django.db import models


class Project(models.Model):
    #dev = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    project_url = models.URLField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

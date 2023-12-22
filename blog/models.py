from django.db import models

# Create your models here.


class post(models.Model):
    # image
    # author
    title = models.CharField(max_length=255, default='Default Title')
    content = models.TextField()

    # tag
    # category

    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now = True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


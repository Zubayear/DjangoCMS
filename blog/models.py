from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


    # for admin, this is to show the title in the db
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]

    def pub_date_pres(self):
        return self.pub_date.strftime('%b %d %Y')
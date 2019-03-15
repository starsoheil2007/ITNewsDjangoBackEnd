from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ManyToManyField(to='Category', blank=False)
    title = models.TextField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    visit_count = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

from django.db import models

class Author(models.Model):
    authorid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=60)
    age=models.IntegerField(max_length=30)
    
    def __unicode__(self):
        return u'%d' % (self.authorid)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authorid = models.IntegerField(max_length=30)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField(max_length=30)
    price=models.IntegerField(max_length=30)
    isbn=models.CharField(primary_key=True)
    def __unicode__(self):
        return self.title

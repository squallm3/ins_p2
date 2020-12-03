from django.db import models


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Word(models.Model):
    entry = models.ManyToManyField(Entry)
    name = models.CharField(max_length=50)

    def __str__(self):
        if len(self.name) > 50:
            return self.name[0:20]
        else:
            return self.name

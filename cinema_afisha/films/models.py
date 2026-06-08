from django.db import models




class Film(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    release_year = models.IntegerField()
    rating =  models.FloatField()
    is_hit = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str___(self):
        return self.title
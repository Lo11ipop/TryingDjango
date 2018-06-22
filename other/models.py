from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)

    class Meta:
        db_table = 't_articles'

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:200] + '...'




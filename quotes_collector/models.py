from django.db import models

#foreign key - когда значение в столбце - ключ в другой таблице
class Author(models.Model):
    name = models.CharField(max_length=150)
    sources = models.ManyToManyField('Source')


class Source(models.Model):
    title = models.CharField(max_length=150)
    authors = models.ManyToManyField(Author)


class Quote(models.Model):
    text = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']




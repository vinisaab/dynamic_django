from django.db import models


class Page(models.Model):
    page = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page

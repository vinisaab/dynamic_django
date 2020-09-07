from django.db import models


class Page(models.Model):
    page = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.page


class Sections(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.section


class Content(models.Model):
    choices = (
        ('T', 'Text'),
        ('E', 'Email'),
        ('P', 'Phone'),
        ('A', 'Address')
    )
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)
    tag = models.CharField(max_length=1, choices=choices)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content

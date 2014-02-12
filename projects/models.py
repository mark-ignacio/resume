from __future__ import unicode_literals
from django.db import models


class Company(models.Model):
    name = models.CharField('Name', max_length=255)
    logo = models.ImageField('Logo', upload_to='/img/companies', blank=True)

    def __unicode__(self):
        return self.name


class Employer(Company):
    pass


class Client(Company):
    pass


class Project(models.Model):
    name = models.CharField('Name', max_length=255)
    description = models.TextField(help_text='Use Markdown syntax and write truncatable first sentences')
    link = models.URLField(blank=True)
    image = models.ImageField('Image', upload_to='img/projects', blank=True,
                              help_text='720p-ish Screenshot or other image')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True, help_text='Leave blank to display "Current"')


    class Meta:
        abstract = True
        ordering = ('-start_date',)

    def __unicode__(self):
        return self.name


class PersonalProject(Project):
    pass


class CommissionedProject(Project):
    employer = models.ForeignKey(Employer, blank=True)
    clients = models.ManyToManyField(Client, blank=True)
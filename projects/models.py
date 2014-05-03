from __future__ import unicode_literals
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
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

    tags = generic.GenericRelation('Tag')

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


class TagCategory(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Tag categories'

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField()
    category = models.ForeignKey(TagCategory, related_name='tags')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.name
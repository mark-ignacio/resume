from __future__ import unicode_literals
from django.db import models


class Taxonomy(models.Model):
    """
    Key-Value store inside a relational database~
    """
    key = models.CharField(max_length=255, unique=True)
    val = models.TextField()

    class Meta:
        verbose_name_plural = 'Taxonomies'

    def __unicode__(self):
        return self.key

    def get_val(self, default=''):
        if self.val:
            return self.val
        else:
            return default
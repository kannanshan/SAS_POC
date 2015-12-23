from __future__ import unicode_literals

from django.db import models

class Ticket_details(models.Model):
    ticket_id = models.IntegerField()
    subject = models.TextField()
    description = models.TextField()
    status = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    priority = models.IntegerField()
    type = models.CharField(max_length=50)
    agent = models.CharField(max_length=50)
    group_name = models.CharField(max_length=50)
    created_at = models.DateField()

    def __str__(self):              # __unicode__ on Python 2
        return self.ticket_id

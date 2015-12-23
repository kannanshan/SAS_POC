from __future__ import unicode_literals

from django.db import models

class TicketDetails(models.Model):
    ticket_id = models.IntegerField(db_index=True)
    subject = models.TextField()
    description = models.TextField()
    status = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    priority = models.IntegerField()
    t_type = models.CharField(max_length=50)
    agent = models.CharField(max_length=50)
    group_name = models.CharField(max_length=50)
    created_at = models.DateField()
    def __unicode__(self):
        return unicode(self.ticket_id)



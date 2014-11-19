from django.db import models

class Legislation(models.Model):
    state = models.CharField(max_length=100)
    bill_number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    session_year = models.CharField(max_length=20)
    def __unicode__(self):
        return self.bill_number + ' (' + self.state + ')'


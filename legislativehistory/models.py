from django.db import models
from django.template.defaultfilters import slugify

class Legislation(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=255) # not SlugField because GAE doesn't support it
    state = models.CharField(max_length=100)
    bill_number = models.CharField(max_length=100)
    session_year = models.CharField(max_length=20)
    def __unicode__(self):
        return self.bill_number + ' (' + self.state + ')'
    def save(self, *args, **kwargs):
        self.slug = str(slugify(self.bill_number))
        super(Legislation, self).save(*args, **kwargs)

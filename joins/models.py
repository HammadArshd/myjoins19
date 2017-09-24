from django.db import models

# Create your models here.
class Join(models.Model):
    email = models.EmailField(unique=True)
    ref_id = models.CharField(max_length=120, default='ABC', unique=True)
    ip_address = models.CharField(max_length=120, default='ABC')
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)

# Python 2.7
    # def __unicode__(self):
    #     return self.email

    # from python 3 onwards
    def __str__(self):
        return self.email

    class Meta:
        unique_together = ("email", "ref_id")

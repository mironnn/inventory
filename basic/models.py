from django.db import models

# Create your models here.

class user (models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name


class device_type (models.Model):
    type = models.CharField(max_length=30)
    def __unicode__(self):
        return self.type


class device (models.Model):
    device_name = models.CharField(max_length=100)
    User = models.ForeignKey(user)
    type = models.ForeignKey(device_type)
    serial_number = models.CharField(max_length=100)
    date_start = models.DateTimeField('Start warranty')
    date_finish = models.DateTimeField('Finish warranty')
    def __unicode__(self):
        return self.device_name



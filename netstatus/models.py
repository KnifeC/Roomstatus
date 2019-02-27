from django.db import models

# Create your models here.

class Netstatus(models.Model):
    device = models.TextField(default=None, blank=True, null=True)
    #updatetime = models.DateTimeField()
    updatetime = models.TextField(default=None, blank=True, null=True)
    ipadress = models.TextField(default=None, blank=True, null=True)
    geoadress = models.TextField(default='Unknown', blank=True, null=True)

    def __str__(self):
        data = {'device':self.device,'updatetime':self.updatetime,'ipadress':self.ipadress,'geoadress':self.geoadress}
        return str(data)

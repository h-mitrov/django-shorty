from django.db import models
from django.contrib.auth.models import User
__author__ = 'cingusoft'


class Url(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    url_field = models.URLField(max_length=500)
    personal = models.BooleanField(default=False)
    personal_slug = models.CharField(max_length=125, blank=True, null=True)
    status = models.CharField(max_length=10)
    private = models.BooleanField(default=False)
    private_password = models.CharField(max_length=25, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    @property
    def is_active(self):
        if self.status == 'Active':
            return True
        return None

    @property
    def is_banned(self):
        if self.status == 'Banned':
            return True
        return None

    @property
    def is_pending(self):
        if self.status == 'Pending':
            return True
        return None

    @property
    def is_refused(self):
        if self.status == 'Refused':
            return True
        return None

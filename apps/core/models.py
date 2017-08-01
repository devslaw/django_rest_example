from django.utils import timezone
from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.modified = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True

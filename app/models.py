from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
"""
начала по 17.36 по ЕКБ

"""
class Appication(models.Model):
    name = models.CharField(max_length=128, verbose_name=_("Название приложения"), default="")
    api_key = models.CharField(max_length=128, verbose_name=_("Ключ API"), default="", unique=True)
   
    def __str__(self):
        return self.name

    def generate_api_key(self):
        return uuid.uuid1()

    def save(self, *args, **kwargs):
        if not self.api_key:
            # New instance
            self.api_key = self.generate_api_key()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Приложение")
        verbose_name_plural = _("Приложения")    


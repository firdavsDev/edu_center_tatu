from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    name = models.CharField(_('name'), max_length=50, blank=True, null=True)
    phone = models.CharField(_('phone'), max_length=50, blank=True, null=True)
    tg_username = models.CharField(
        _('telegram username'), max_length=50, blank=True, null=True)
    is_asnwered = models.BooleanField(_('is answered'), default=False)
    # Timestamps
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
        ordering = ('-created',)

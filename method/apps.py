from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MethodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'method'
    verbose_name = _('method')

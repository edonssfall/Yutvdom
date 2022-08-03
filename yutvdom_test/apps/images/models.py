from django.db import models
from django.utils.translation import gettext_lazy as _


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=_('created images'))
    title = models.CharField(_("Title image"), max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to=_("images%Y%m%d"))
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

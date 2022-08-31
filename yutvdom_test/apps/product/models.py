from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("Category"), max_length=255, db_index=True, unique=True)
    slug = models.SlugField(_("Slug"), max_length=255, db_index=True, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = _("Category")
        verbose_name_plural = _("Category")

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name=_("Category"))
    name = models.CharField(_("Name"), max_length=255, db_index=True)
    slug = models.SlugField(_("Slug"), max_length=255, db_index=True)
    image = models.ImageField(_("Image"), upload_to='products%Y%m%d', blank=True)
    description = models.CharField(_("Description"), max_length=255)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(_("Stock"))
    available = models.BooleanField(_("Available"), default=False)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now_add=True)

    class Meta:
        ordering = ("name",)
        index_together = (("id", "slug"),)

    def __str__(self):
        return self.name

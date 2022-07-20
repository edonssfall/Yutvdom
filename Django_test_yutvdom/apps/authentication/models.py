from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=150)

    is_admin = models.BooleanField(default=False)

    def __str__(self):
        user = self.email + " " + self.is_admin
        return user

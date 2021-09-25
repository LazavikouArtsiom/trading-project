from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save

from .signals import create_related_to_user_models_postsave

class User(AbstractUser):
    
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    created = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

post_save.connect(create_related_to_user_models_postsave, sender=User)
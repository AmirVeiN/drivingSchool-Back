from django.contrib.auth.models import BaseUserManager
from . import constants as user_constants


class UserManager(BaseUserManager):
    def create_user(self, name, address, codemeli ,telephone, password=None, **extra_fields):
        if not codemeli:
            raise ValueError("The Codemeli field must be set")
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("user_type", user_constants.HONARJOO)
        user = self.model(name=name, address=address, codemeli=codemeli, telephone=telephone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, address, codemeli ,telephone, password=None , **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("user_type", user_constants.ADMIN)
        user = self.model(name=name, address=address, codemeli=codemeli, telephone=telephone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, name, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        # kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, name, password, **kwargs)

    def create_user(self, email, name, password, **kwargs):
        if not email:
            raise ValueError(_("You must provide an email address"))
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **kwargs)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), max_length=254, unique=True)
    name = models.CharField(_("name"), max_length=50)
    # birthday = models.DateField(_("birthdate"), auto_now=False, auto_now_add=False)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    is_staff = models.BooleanField(_("staff"), default=False)
    is_active = models.BooleanField(_("active"), default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "name",
    ]
    #  "birthday"]

    def __str__(self):
        return self.email

    # @property
    # def age(self):
    #     return timezone.now().date() - self.birthday

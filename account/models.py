from django.db import models
import uuid
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import UserManger


def validate_email_address(value):

    try:
        validate_email(value=str(value).lower())
    except Exception as e:
        raise ValidationError('email is not valid')



class User(AbstractBaseUser,PermissionsMixin):

    id=models.UUIDField(
        default=uuid.uuid4,
        db_index=True,
        blank=False,
        db_column="id",
        name="id",
        db_comment="id",
        verbose_name="id",
        help_text="id",
        editable=False,
        unique=True,
        primary_key=True,

    )


    email=models.EmailField(
        db_index=True,
        blank=False,
        unique=True,
        max_length=200,
        db_column="email",
        db_comment="email",
        verbose_name="user email",
        help_text="user email",
        validators=[validate_email_address]
    )


    username=models.CharField(
        max_length=150,
        db_index=True,
        blank=True,
        unique=True,
        null=True,
        help_text="username",
        verbose_name="username",

    )

    is_admin=models.BooleanField(
        default=False,
        db_index=True,
        verbose_name="is user admin",
        help_text="is user admin",
    )

    
    is_staff=models.BooleanField(
        default=False,
        db_index=True,
        verbose_name="is user staff",
        help_text="is user staff",
    )



    is_active = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name="is user active",
        help_text="is user active"
    )

    

    is_superuser = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name="is user superuser",
        help_text="is user superuser",
    )


    date_joined = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="date joined",
        help_text="date joined"
    )

    user_ip=models.GenericIPAddressField(
        db_index=True,
        blank=True,
        null=True,
        verbose_name="user ip address",
        help_text="user ip address",
    )



    created = models.DateTimeField(
        auto_now_add=True,
        help_text="created time",
        verbose_name="created time",
        db_index=True,

    )

    updated = models.DateTimeField(
        auto_now=True,
        help_text="updated time",
        verbose_name="updated time",
        db_index=True,

    )

    USERNAME_FIELD="email"

    REQUIRED_FIELDS=[
        "username",
        
    ]

    def has_perm(self, perm, obj = ...):
        return self.is_admin and self.is_active and self.is_superuser
    
    def has_module_perms(self, app_label):
        return True
    



    def __str__(self):
        return str(self.email)
    


    objects=UserManger()

    class Meta:

        verbose_name="user"
        verbose_name_plural="user"
        ordering=[
            "created"
        ]








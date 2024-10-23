from django.db import models
from django.core.validators import FileExtensionValidator

class CommonModel(models.Model):


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









class FirstSlider(CommonModel):


    image=models.ImageField(
        db_index=True,
        verbose_name="image",
        help_text="image",
        validators=[FileExtensionValidator(
            allowed_extensions=[
                "png","jpeg",
                "jpg"
            ]
        )
        ]
    )

    title=models.CharField(
        max_length=400,
        db_index=True,
        blank=True,
        null=True,
        verbose_name="enter title",
        help_text="enter title"
    )

    description=models.TextField(
        max_length=400,
        db_index=True,
        blank=True,
        null=True,
        verbose_name="enter description",
        help_text="enter description"
    )

    is_active=models.BooleanField(
        default=False,
        blank=True,
        null=True,
        verbose_name="is active",
        help_text="is active"
    )




    
    def __str__(self):
        return str(self.title)
    






class Service(CommonModel):


    image=models.ImageField(
        db_index=True,
        verbose_name="image",
        help_text="image",
        validators=[FileExtensionValidator(
            allowed_extensions=[
                "png","jpeg",
                "jpg"
            ]
        )
        ]
    )


    title=models.CharField(
        max_length=400,
        db_index=True,
        blank=True,
        null=True,
        verbose_name="enter title",
        help_text="enter title"
    )

    description=models.TextField(
        max_length=400,
        db_index=True,
        blank=True,
        null=True,
        verbose_name="enter description",
        help_text="enter description"
    )

    is_active=models.BooleanField(
        default=False,
        blank=True,
        null=True,
        verbose_name="is active",
        help_text="is active"
    )




class ServiceFeatcher(models.Model):



    title=models.CharField(
        max_length=400,
        db_index=True,
        blank=True,
        null=True,
        verbose_name="enter title",
        help_text="enter title"
    )

    service=models.ForeignKey(
        to=Service,
        db_index=True,
        db_column="service",
        # to_field="id",
        on_delete=models.CASCADE,
    )
    
    is_active=models.BooleanField(
        default=False,
        blank=True,
        null=True,
        verbose_name="is active",
        help_text="is active"
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

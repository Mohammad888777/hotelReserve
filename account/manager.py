from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class  UserManger(BaseUserManager):


    def create(self, email,password=None):

        try:
            validate_email(email)
        except Exception as e:
            raise ValidationError("email is not valid")

        if self.filter(email=self.normalize_email(email)).exists():
            raise ValidationError('email already exists ')
        

        
        new_user=self.model(
            email=self.normalize_email(email),
        )

        new_user.set_password(password)
        new_user.save(using=self._db)
        

        return new_user
    

    

    def create_superuser(self,email,username,password=None):

        try:
            validate_email(email)
        except Exception as e:
            raise ValidationError("email is not valid")

        if self.filter(email=self.normalize_email(email)).exists():
            raise ValidationError('email already exists ')
        
        if self.filter(username=username).exists():
            raise ValidationError("username already exsists")
        
        new_user=self.model(
                    email=self.normalize_email(email),
                    username=username,
                )
        
        new_user.set_password(password)

        new_user.save(using=self._db)
        new_user.is_active=True
        new_user.is_admin=True
        new_user.is_staff=True
        new_user.is_superuser=True
        new_user.save(using=self._db)
        

        return new_user
    
    
    


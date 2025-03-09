from django.db import models
# for create a custom user and admin panel
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils.translation import ugettext_lazy


class MyUserManager(BaseUserManager):
    # a custom  manager to deal the email as a unique identifier
    
    def _create_user(self,email,password,**extra_fields):
        #creates and saves a user with given email and password
        if not email:
            raise ValueError("email must be set")
        email= self.normalize_email(email)
        user= self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault( ' is_staff', True)
        extra_fields. setdefault( ' is_superuser', True)
        extra_fields. setdefault( 'is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError( 'Superuser must have is staff-True')
        if extra_fields.get( 'is_superuser') is not True:
            raise ValueError( 'Superuser must have is superuser-True')
        return self._create_user(email, password, **extra_fields) 

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)

    is_staff = models.BooleanField(
        ugettext_lazy("staff status"),
        default=False,
        help_text=ugettext_lazy("Designates whether the user can log into this site.")
    )

    is_active = models.BooleanField(
       ugettext_lazy("active"),
        default=True,
        help_text= ugettext_lazy("Designates whether this user should be treated as active. Unselect this instead of deleting accounts.")
    )

    USERNAME_FIELD = "email"

    objects = MyUserManager()

    def __str__(self):
        return self.email        
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
        
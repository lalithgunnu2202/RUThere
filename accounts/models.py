from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("All Fields are required")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # ✅ hashes the password
        user.save(using=self._db)    # ✅ saves correctly with DB context
        return user

    
    def create_superuser(self,username,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        return self.create_user(username,password,**extra_fields)
    
class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50,unique=True)
    last_login = models.DateTimeField(auto_now=True)
    # phone_number = models.CharField(max_length=10,unique=True)
    email = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS=['email']
    ROLE_CHOICES=(
        ('club','Club'),
        ('student','Student'),
    )
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='student')
    objects = CustomUserManager()
    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
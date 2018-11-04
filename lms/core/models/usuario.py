from django.db import models
from datetime import date
from django.contrib.auth.models import(
     AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):
     def create_user(self, login, password=None, active=True, is_staff=False, is_admin=False):
          if not password:
               raise ValueError("Senha nao pode ser vazia")

          user_obj = self.model(
               login = login
          )
          user_obj.set_password(password)
          user_obj.staff = is_staff
          user_obj.admin = is_admin
          user_obj.active = active
          user_obj.save(using=self._db)
          return user_obj
     
     def create_staffuser(self, login, password=None):
          user = self.create_user(login, password=password, is_staff=True)
          return user

     def create_superuser(self, login, password=None):
          user = self.create_user(login, password=password, is_staff=True, is_admin=True)
          return user

class User(AbstractBaseUser):
     login          = models.CharField(max_length=100, unique=True)
     dtExpiracao    = models.DateField(default=date(1900, 1, 1))
     active         = models.BooleanField(default=True) #can login
     staff          = models.BooleanField(default=False) # staff user
     admin          = models.BooleanField(default=False) # superuser

     USERNAME_FIELD = 'login'
     REQUIRED_FIELDS = []

     objects = UserManager()

     def __str__(self):
          return self.login
    
     def get_full_name(self):
          return self.login

     def get_short_name(self):
          return self.login

     def has_perm(self, perm, obj=None):
          return True

     def has_module_perms(self, app_label):
          return True

     @property
     def is_staff(self):
          return self.staff

     @property
     def is_admin(self):
          return self.admin

     @property
     def is_active(self):
          return self.active
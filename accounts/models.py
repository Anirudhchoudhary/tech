from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser)
# User	|Role
# PS	|Super User
# Sec	|Super User
# Mandal Level Officer	|Inter User
# District Level Officer	|Inter User
# HeadMaster|	Modifier
# Contractor|	Modifier
# Auditor	|Modifier
# Admin|	Admin

# ROLE = (
#     ('')
# )

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    Sec = models.BooleanField(default=False)
    Mandal_Officer = models.BooleanField(default=False)
    District_Officer = models.BooleanField(default=False)
    HeadMaster = models.BooleanField(default=False)
    Contractor = models.BooleanField(default=False)
    Auditor = models.BooleanField(default=False)


    # notice the absence of a "Password field", that's built in.
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):                                         
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active  

    @property
    def is_sec(self):
        "Is the user sec?"
        return self.Sec

    @property
    def is_manadal_officer(self):
        "Is the user mandal_officer?"
        return self.Mandal_Officer

    @property
    def is_district_officer(self):
        "Is the user District Officer?"
        return self.District_Officer

    @property
    def is_headmaster(self):
        "Is the user Headmaster?"
        return self.HeadMaster

    @property
    def is_contractor(self):
        "Is the user Contractor?"
        return self.Contractor

    @property
    def is_auditor(self):
        "Is the user Auditor?"
        return self.Auditor
   
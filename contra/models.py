from django.db import models
from django.urls import reverse
from accounts.models import User
from itertools import chain
# Create your models here.

STATUS = (
    ('APPROVED','AP'),
    ('NOT APPROVED','NP')
)


class ContractorManager(models.Manager):
  

    def get_contract(self , request):
        user = request.user
        qs = None 
        if user.is_authenticated and user.is_contractor:
            if user is not None:
                qs = Contractor.objects.filter(user = user)         
            return qs
        elif user.is_authenticated:
            if user.is_manadal_officer or user.is_district_officer or user.is_headmaster or user.is_auditor:
                qs = Contractor.objects.all()
                return qs         
        else:
            return qs



class Contractor(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null =True , blank = True )
    name = models.CharField(max_length = 256 , null =False , blank = False , help_text = 'Your Busniess name')
    Money = models.PositiveIntegerField(null = False , blank = False,help_text = 'Money for work')
    Time = models.PositiveIntegerField(null = False , blank = False,help_text = 'Time required for work')
    area = models.PositiveIntegerField(null = False , blank = False,help_text = 'area of work')
    Image = models.ImageField(null = True , blank = True, help_text = 'proposed work image')
    email = models.EmailField(null = False , blank = False , help_text = 'Email to connect you')
    Status = models.CharField(max_length = 230 , choices = STATUS, null = True , blank = True)
    Reason = models.CharField(max_length = 230, null = True , blank = True)

    objects = ContractorManager()

    def get_absolute_url(self):
        return reverse("contract:contract_details" , kwargs = {"pk":self.pk})

    def __str__(self):
        return self.name


# class SchoolManager(models.Manager):
  
#  g = School.objects.filter(contractor = school)
    # def get_school(self,request):
    #     user = request.user
    #     qs = None 
    #     if user.is_authenticated and user.is_contractor:
    #         if user is not None:
    #             qs = School.objects.filter(contractor = Contractor.objects.get_contract(request = request))
    #             print(qs) 
    #         return qs
    #     else:
    #         return qs


class School(models.Model):
    schoolcode = models.PositiveIntegerField(null = False , blank = False)
    school_name = models.CharField(max_length = 257 , null = False , blank = False)
    District = models.CharField(max_length = 259)
    Constituencies = models.CharField(max_length = 257 , null = False , blank = False)
    Mandal = models.CharField(max_length = 259)
    lat = models.PositiveIntegerField()
    Long = models.PositiveIntegerField()
    Amentier_Required = models.CharField(max_length = 234 , null = True , blank = True)
    School_level = models.CharField(max_length = 234 , null = True , blank = True)
    school_Area = models.CharField(max_length = 234 , null = True , blank = True)
    contractor = models.ForeignKey(Contractor , on_delete = models.CASCADE , null =True , blank = True)
    Teacher = models.PositiveIntegerField(null = True , blank = True)
    student =  models.PositiveIntegerField(null = True , blank = True)
    support_staff = models.PositiveIntegerField(null = True , blank = True)

    # objects = SchoolManager()

    def __str__(self):
        return self.school_name
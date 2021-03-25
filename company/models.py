from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse




class Company(models.Model):
    contract_address = models.CharField(max_length=42,
                                        blank=True,
                                        null=True)
    published = models.BooleanField(default=False)
    # created_by = models.ForeignKey('users.Member',
    #                                related_name='+',
    #                                on_delete=models.SET_NULL,
    #                                null=True)

    logo = models.ImageField(null=True)
    name = models.CharField(max_length=512,
                            null=False,
                            blank=False)
    tax_number = models.CharField(max_length=64,
                                  null=False,
                                  blank=False)
    legal_address = models.CharField(max_length=255)
    work_sector = models.CharField(max_length=512)
    date_created = models.DateField(null=True,
                                    blank=True)
    site = models.URLField(null=True,
                           blank=True)
    description = models.TextField(blank=False,
                                   null=False)
    phone = models.CharField(max_length=31)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
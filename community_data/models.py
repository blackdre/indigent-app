from django.db import models


class Person(models.Model):
    # personal details section
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=13, unique=True)
    contact_number = models.CharField(max_length=200, unique=True)
    # Gender selection fields
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER)
    # employment status selection fields
    EMPLOYMENT_STATUS = (
        ('U', 'Unemployed'),
        ('E', 'Employed'),
        ('S', 'Self-Employed'),
    )
    employment_status = models.CharField(
        max_length=1, choices=EMPLOYMENT_STATUS)
    # ownership status
    OWNERSHIP_STATUS = (
        ('O', 'Owner'),
        ('T', 'Tenant')
    )
    ownership_status = models.CharField(max_length=1, choices=OWNERSHIP_STATUS)

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'

    def __str__(self):
        return self.id_number


class Residence(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    address = models.TextField()
    area = models.CharField(max_length=200)
    ward_number = models.CharField(max_length=10)
    water_meter = models.CharField(max_length=200)
    electricity_meter = models.CharField(max_length=200)

    def __str__(self):
        return self.area

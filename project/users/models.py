from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_Registration_Table(models.Model):

    STATUS = [
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'), 
        ('rejected', 'Rejected'),
        ('suspended', 'Account Suspended') 
        ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cellphone = models.CharField(null=True)
    study_path = models.CharField(null=True)
    level = models.CharField(null=True)
    github_url = models.URLField()
    full_name = models.CharField(null=True)
    active_status = models.CharField(
        default='Pending Approval', choices=STATUS
    )

    
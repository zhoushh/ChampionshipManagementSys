from django.db import models
#
# # Create your models here.

from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from orgnisation.models import Orgnisation

class UserProfile(AbstractUser):
    
    userType_choice = (
        ('individual', '个人'),
        ('club', '俱乐部'),
        ('association', '组织方')
    )
    
    userCode = models.CharField('用户代码', max_length=10, null=True)
    userType = models.CharField('用户类型', max_length=16, choices=userType_choice, default='individual')
    userInOrg = models.ForeignKey(Orgnisation, verbose_name='用户组织', on_delete=models.SET_NULL, null=True, blank=True)
    
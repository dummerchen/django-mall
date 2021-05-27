from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):

    mobile=models.CharField(max_length=11,unique=True,verbose_name='phone number')

    class Meta:
        # 表名规范 db_name
        db_table='db_user'
        verbose_name='user_name'
        verbose_name_plural=verbose_name


from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, name, password=None):
        """
        Creates and saves a User with the given phone_number, date of
        birth and password.
        """
        if not phone_number:
            raise ValueError('Users must have an phone_number address')

        user = self.model(
            phone_number=self.normalize_phone_number(phone_number),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name, password):
        """
        Creates and saves a superuser with the given phone_number, date of
        birth and password.
        """
        user = self.create_user(
            phone_number,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    job_tuple = (
        (0, u'管理员'),
        (1, u'网络客服主管'),
        (2, u'网络客服'),
        (3, u'前台'),
        (4, u'咨询师'),
        (5, u'美容师'),
    )
    job = models.IntegerField(choices=job_tuple, verbose_name="职位", default=0)

    phone_number = models.CharField(
        verbose_name='手机号',
        max_length=255,
        unique=True,
    )
    name = models.CharField(verbose_name='姓名', max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    # 用户等级，0代表总部，1代表加盟商，2代表加盟商所属店员
    admin_level = models.IntegerField(default=2)
    # 父节点id，用于设置用户间的归属关系
    parent_id = models.IntegerField(default=0)
    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = u'账号'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

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
        # Simplest possible answer: All admins are staff
        return self.is_admin
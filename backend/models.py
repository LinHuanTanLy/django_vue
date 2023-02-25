import uuid

from django.db import models


# Create your models here.
class Link(models.Model):
    linkId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    linkDescription = models.CharField(max_length=200, verbose_name="链接描述")
    linkUrl = models.CharField(max_length=200, verbose_name="链接地址")
    linkRemark = models.CharField(max_length=200, verbose_name='链接备注')
    userName = models.CharField(max_length=50, verbose_name='账户', default='niki')
    passWord = models.CharField(max_length=20, verbose_name='密码', default='123456')

    def __unicode__(self): return self.linkUrl

    def __str__(self): return self.linkUrl

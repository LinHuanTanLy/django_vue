from django.db import models


# Create your models here.
class Link(models.Model):
    linkDescription = models.CharField(max_length=200, verbose_name="链接描述")
    linkUrl = models.CharField(max_length=200, verbose_name="链接地址")
    linkRemark = models.CharField(max_length=200, verbose_name='链接备注')

    def __unicode__(self): return self.linkUrl

    def __str__(self): return self.linkUrl

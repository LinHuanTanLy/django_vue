# Generated by Django 4.1.7 on 2023-02-25 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='PassWord',
            field=models.CharField(default='123456', max_length=20, verbose_name='密码'),
        ),
        migrations.AddField(
            model_name='link',
            name='userName',
            field=models.CharField(default='niki', max_length=50, verbose_name='账户'),
        ),
    ]

# Generated by Django 2.0.3 on 2018-05-29 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userCode',
            field=models.CharField(max_length=10, null=True, verbose_name='用户代码'),
        ),
    ]

# Generated by Django 2.0.3 on 2018-06-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='championship',
            name='chsID',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='赛事代码'),
        ),
    ]

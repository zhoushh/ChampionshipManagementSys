# Generated by Django 2.0.3 on 2018-06-02 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orgnisation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chsName', models.CharField(max_length=64, null=True, verbose_name='赛事名称')),
                ('chsCode', models.CharField(max_length=9, verbose_name='赛事代码')),
                ('chsType', models.CharField(choices=[('league', '联赛'), ('cup', '杯赛')], max_length=8, verbose_name='赛事类型')),
                ('capacity', models.IntegerField(verbose_name='参赛队伍数量')),
                ('range', models.CharField(choices=[('national', '国家级'), ('regional', '地区级'), ('local', '地方级')], max_length=16, verbose_name='赛事范围')),
                ('startTime', models.DateField(null=True, verbose_name='开始日期')),
                ('endTime', models.DateField(null=True, verbose_name='结束日期')),
                ('orgBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orgnisation.Orgnisation', verbose_name='承办组织')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateToPlay', models.DateField()),
                ('techStastics', models.FileField(upload_to='E:/gfile/Match')),
                ('belongTo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='championship.Championship', verbose_name='所属赛事')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamType', models.CharField(choices=[('amateur', '业余'), ('professional', '专业')], max_length=32, verbose_name='球队类型')),
                ('teamName', models.CharField(max_length=64, unique=True, verbose_name='球队名称')),
                ('playerList', models.FileField(upload_to='E:/gfile/Team/player_lists')),
                ('belongTo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orgnisation.Orgnisation', verbose_name='所属组织')),
            ],
        ),
    ]

# Generated by Django 2.0.3 on 2018-06-06 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0008_championship_team_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimetableForLeague',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_amount', models.IntegerField(null=True)),
                ('detail', models.TextField(null=True)),
                ('belong_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='championship.Championship', verbose_name='所属赛事')),
            ],
        ),
    ]
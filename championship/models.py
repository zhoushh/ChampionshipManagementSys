from django.db import models
from orgnisation.models import Orgnisation


# Create your models here.


class Championship(models.Model):
	chsType_choice = (
		('league', '联赛'),
		('cup', '杯赛')
	)
	
	range_choice = (
		('national', '国家级'),
		('regional', '地区级'),
		('local', '地方级')
	)
	
	chsName = models.CharField('赛事名称', max_length=64, null=True)
	chsCode = models.CharField('赛事代码', max_length=9, null=True)
	chsType = models.CharField('赛事类型', max_length=8, choices=chsType_choice)
	capacity = models.IntegerField('参赛队伍数量')
	range = models.CharField('赛事范围', max_length=16, choices=range_choice)
	orgBy = models.ForeignKey(Orgnisation, verbose_name='承办组织', on_delete=models.SET_NULL, null=True, blank=True)
	startTime = models.DateField('开始日期', null=True)
	endTime = models.DateField('结束日期', null=True)
	rank_for_league = models.FileField(upload_to='Championship/league', null=True)
	rank_for_cup = models.FileField(upload_to='Championship/cup', null=True)
	timetable = models.FileField(upload_to='Championship/timetable', null=True)
	
	def __str__(self):
		return self.chsName


class Team(models.Model):
	teamType_choice = (
		('amateur', '业余'),
		('professional', '专业')
	)
	
	teamType = models.CharField('球队类型', max_length=32, choices=teamType_choice)
	teamName = models.CharField('球队名称', max_length=64, unique=True)
	belongTo = models.ForeignKey(Orgnisation, verbose_name='所属组织', on_delete=models.SET_NULL, null=True, blank=True)
	playerList = models.FileField(upload_to='Team/player_lists', null=True)
	playerStatistics = models.FileField(upload_to='Team/player_statistics', null=True)
	
	def __str__(self):
		return self.teamName


class Match(models.Model):
	belongTo = models.ForeignKey(Championship, verbose_name='所属赛事', on_delete=models.SET_NULL, null=True, blank=True)
	dateToPlay = models.DateField()
	techStastics = models.FileField(upload_to='Match', null=True)

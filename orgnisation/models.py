from django.db import models


# Create your models here.

class Region(models.Model):
	regionID = models.CharField('地区代码', max_length=6, primary_key=True)
	province = models.CharField('省份', max_length=32)
	city = models.CharField('城市', max_length=32)
	district = models.CharField('县市区', max_length=32, null=True)
	
	def __str__(self):
		return self.province + self.city + self.district


class Orgnisation(models.Model):
	orgType_choice = (
		('club', '俱乐部'),
		('association', '组织方'),
		('group', '民间团体')
	)
	
	orgID = models.CharField('组织代码', max_length=16)
	orgName = models.CharField('名称', max_length=64, unique=True)
	orgType = models.CharField('组织类型', max_length=16, choices=orgType_choice)
	region = models.ForeignKey(Region, verbose_name='组织地区', on_delete=models.SET_NULL, null=True, blank=True)
	
	def __str__(self):
		return self.orgName
from django.db import models

# Create your models here.
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser



class Base(models.Model):

    flag_choices = (
        ('0','非僵尸'),
        ('1','僵尸')
    )

    # enterprise_id = models.CharField('企业ID',max_length=50,default='')
    register = models.CharField('注册时间',max_length=50, default='')
    flag = models.CharField('是否为僵尸企业',max_length=10,choices=flag_choices,default='NA')
    industry = models.CharField('行业',max_length=100,default='')
    registered_fund = models.CharField('注册资本',max_length=50,null=True,blank=True)
    # image = models.ImageField(upload_to='image/%Y%m',default='image/default.png',max_length=100)
    region = models.CharField('区域', max_length=100, default='')
    type = models.CharField('企业类型', max_length=100, default='')
    controller_type = models.CharField('控制人类型', max_length=100, default='')
    controller_hold = models.CharField('控制人持股', max_length=100, default='')

    class Meta:
        verbose_name = '企业基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.enterprise_id



class Knowledge(models.Model):
    patent_choices = (
        ('0', '无专利'),
        ('1', '有专利')
    )
    brand_choices = (
        ('0', '无商标'),
        ('1', '有商标')
    )
    copyright_choices = (
        ('0', '无著作权'),
        ('1', '有著作权')
    )

    enter = models.ForeignKey(Base, verbose_name='企业ID', on_delete=models.CASCADE)
    patent = models.CharField('专利', max_length=10, choices=patent_choices, default='NA')
    brand = models.CharField('商标', max_length=10, choices=brand_choices, default='NA')
    copyright = models.CharField('著作权', max_length=10, choices=copyright_choices, default='NA')

    class Meta:
        verbose_name = '企业知识产权信息'
        verbose_name_plural = verbose_name



class Money_report(models.Model):
    enter = models.ForeignKey(Base, verbose_name='企业ID', on_delete=models.CASCADE)
    year = models.CharField('year', max_length=50, default='')
    bond_limit = models.CharField('债权融资额度', max_length=100, default='')
    bond_cost = models.CharField('债权融资成本', max_length=100, default='')
    stock_limit = models.CharField('股权融资额度', max_length=100, default='')
    stock_cost = models.CharField('股权融资成本', max_length=100, default='')
    trade_limit = models.CharField('内部融资和贸易融资额度', max_length=100, default='')
    trade_cost = models.CharField('内部融资和贸易融资成本', max_length=100, default='')
    item_limit = models.CharField('项目融资和政策融资额度', max_length=100, default='')
    item_cost = models.CharField('项目融资和政策融资成本', max_length=100, default='')
    class Meta:
        verbose_name = '企业金融报表信息'
        verbose_name_plural = verbose_name


class Year_report(models.Model):
    enter = models.ForeignKey(Base, verbose_name='企业ID', on_delete=models.CASCADE)
    year = models.CharField('year', max_length=50, default='')
    # employees = models.CharField('从业人数',max_length=100, default='')
    total_assets = models.CharField('资产总额', max_length=100, default='')
    total_liabilities = models.CharField('负债总额', max_length=100, default='')
    revenue = models.CharField('营业总收入', max_length=100, default='')
    main_revenue = models.CharField('主营业务收入', max_length=100, default='')
    total_profit = models.CharField('利润总额', max_length=100, default='')
    retained_profit = models.CharField('净利润', max_length=100, default='')
    total_tax = models.CharField('纳税总额', max_length=100, default='')
    owner_equity = models.CharField('所有者权益合计', max_length=100, default='')

    class Meta:
        verbose_name = '企业年度报表信息'
        verbose_name_plural = verbose_name

# Generated by Django 3.0.6 on 2020-05-27 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register', models.CharField(default='', max_length=50, verbose_name='注册时间')),
                ('flag', models.CharField(choices=[('0', '非僵尸'), ('1', '僵尸')], default='NA', max_length=10, verbose_name='是否为僵尸企业')),
                ('industry', models.CharField(default='', max_length=100, verbose_name='行业')),
                ('registered_fund', models.CharField(blank=True, max_length=50, null=True, verbose_name='注册资本')),
                ('region', models.CharField(default='', max_length=100, verbose_name='区域')),
                ('type', models.CharField(default='', max_length=100, verbose_name='企业类型')),
                ('controller_type', models.CharField(default='', max_length=100, verbose_name='控制人类型')),
                ('controller_hold', models.CharField(default='', max_length=100, verbose_name='控制人持股')),
            ],
            options={
                'verbose_name': '企业基本信息',
                'verbose_name_plural': '企业基本信息',
            },
        ),
        migrations.CreateModel(
            name='Year_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default='', max_length=50, verbose_name='year')),
                ('total_assets', models.CharField(default='', max_length=100, verbose_name='资产总额')),
                ('total_liabilities', models.CharField(default='', max_length=100, verbose_name='负债总额')),
                ('revenue', models.CharField(default='', max_length=100, verbose_name='营业总收入')),
                ('main_revenue', models.CharField(default='', max_length=100, verbose_name='主营业务收入')),
                ('total_profit', models.CharField(default='', max_length=100, verbose_name='利润总额')),
                ('retained_profit', models.CharField(default='', max_length=100, verbose_name='净利润')),
                ('total_tax', models.CharField(default='', max_length=100, verbose_name='纳税总额')),
                ('owner_equity', models.CharField(default='', max_length=100, verbose_name='所有者权益合计')),
                ('enter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.Base', verbose_name='企业ID')),
            ],
            options={
                'verbose_name': '企业年度报表信息',
                'verbose_name_plural': '企业年度报表信息',
            },
        ),
        migrations.CreateModel(
            name='Money_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default='', max_length=50, verbose_name='year')),
                ('bond_limit', models.CharField(default='', max_length=100, verbose_name='债权融资额度')),
                ('bond_cost', models.CharField(default='', max_length=100, verbose_name='债权融资成本')),
                ('stock_limit', models.CharField(default='', max_length=100, verbose_name='股权融资额度')),
                ('stock_cost', models.CharField(default='', max_length=100, verbose_name='股权融资成本')),
                ('trade_limit', models.CharField(default='', max_length=100, verbose_name='内部融资和贸易融资额度')),
                ('trade_cost', models.CharField(default='', max_length=100, verbose_name='内部融资和贸易融资成本')),
                ('item_limit', models.CharField(default='', max_length=100, verbose_name='项目融资和政策融资额度')),
                ('item_cost', models.CharField(default='', max_length=100, verbose_name='项目融资和政策融资成本')),
                ('enter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.Base', verbose_name='企业ID')),
            ],
            options={
                'verbose_name': '企业金融报表信息',
                'verbose_name_plural': '企业金融报表信息',
            },
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patent', models.CharField(choices=[('0', '无专利'), ('1', '有专利')], default='NA', max_length=10, verbose_name='专利')),
                ('brand', models.CharField(choices=[('0', '无商标'), ('1', '有商标')], default='NA', max_length=10, verbose_name='商标')),
                ('copyright', models.CharField(choices=[('0', '无著作权'), ('1', '有著作权')], default='NA', max_length=10, verbose_name='著作权')),
                ('enter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.Base', verbose_name='企业ID')),
            ],
            options={
                'verbose_name': '企业知识产权信息',
                'verbose_name_plural': '企业知识产权信息',
            },
        ),
    ]

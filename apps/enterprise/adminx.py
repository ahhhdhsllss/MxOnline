# organization/adminx.py

import xadmin

from .models import Money_report, Knowledge, Base, Year_report


class BaseAdmin(object):
    '''企业基本信息'''

    list_display = [ 'region', 'industry', 'type', 'flag']
    search_fields = [ 'industry']
    list_filter = [ 'industry', 'flag']


class KnowledgeAdmin(object):
    '''企业知识产权'''

    list_display = ['enter', 'patent', 'brand', 'copyright']
    search_fields = ['enter', 'patent', 'brand', 'copyright']
    list_filter = ['enter', 'patent', 'brand', 'copyright']


class Money_reportAdmin(object):
    '''企业金融报表'''

    list_display = ['enter', 'bond_cost', 'stock_cost', 'trade_cost', 'item_cost']
    search_fields = ['enter', 'year']
    list_filter = ['enter', 'year']


class Year_reportAdmin(object):
    '''企业年度报表'''

    list_display = ['enter', 'total_assets', 'revenue', 'total_profit', 'retained_profit', 'total_tax']
    search_fields = ['enter', 'year']
    list_filter = ['enter', 'year']


xadmin.site.register(Money_report, Money_reportAdmin)
xadmin.site.register(Knowledge, KnowledgeAdmin)
xadmin.site.register(Base, BaseAdmin)
xadmin.site.register(Year_report, Year_reportAdmin)

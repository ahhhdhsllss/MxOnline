# organization/adminx.py

import xadmin

from .models import Money_report, Knowledge, Base, Year_report


class BaseAdmin(object):
    '''企业基本信息'''

    list_display = ['enterprise_id', 'region', 'industry', 'type', 'flag']
    search_fields = ['enterprise_id', 'industry']
    list_filter = ['enterprise_id', 'industry', 'flag']


class KnowledgeAdmin(object):
    '''企业知识产权'''

    list_display = ['enterprise_id', 'patent', 'brand', 'copyright']
    search_fields = ['enterprise_id', 'patent', 'brand', 'copyright']
    list_filter = ['enterprise_id', 'patent', 'brand', 'copyright']


class Money_reportAdmin(object):
    '''企业金融报表'''

    list_display = ['enterprise_id', 'bond_cost', 'stock_cost', 'trade_cost', 'item_cost']
    search_fields = ['enterprise_id', 'year']
    list_filter = ['enterprise_id', 'year']


class Year_reportAdmin(object):
    '''企业年度报表'''

    list_display = ['enterprise_id', 'total_assets', 'revenue', 'total_profit', 'retained_profit', 'total_tax']
    search_fields = ['enterprise_id', 'year']
    list_filter = ['enterprise_id', 'year']


xadmin.site.register(Money_report, Money_reportAdmin)
xadmin.site.register(Knowledge, KnowledgeAdmin)
xadmin.site.register(Base, BaseAdmin)
xadmin.site.register(Year_report, Year_reportAdmin)

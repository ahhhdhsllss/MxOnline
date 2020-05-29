from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from enterprise.models import Base, Knowledge, Money_report, Year_report
from django.db.models import Q,Count


class EnterView(View):
    '''课程机构'''

    def get(self, request):
        # 所有企业
        all_orgs = Base.objects.all()

        # 所有金融报表
        # all_city = RegionDict.objects.all()

        # 机构搜索功能
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            # 在name字段进行操作,做like语句的操作。i代表不区分大小写
            # or操作使用Q
            all_orgs = all_orgs.filter(Q(enterprise_id__icontains=search_keywords) | Q(type__icontains=search_keywords))
        # 行业筛选
        reg = request.GET.get('cy','')
        if reg:
            all_orgs = all_orgs.filter(region=reg)

        # 类别筛选
        category = request.GET.get('ct','')
        if category:
            all_orgs = all_orgs.filter(industry=category)

        # 按注册时间排名企业
        hot_orgs = all_orgs.order_by('-register')[:3]
        # 企业类型和区域筛选
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "type":
                all_orgs = all_orgs.order_by("-type")
            elif sort == "region":
                all_orgs = all_orgs.order_by("-region")
        # 有多少家机构
        org_nums = all_orgs.count()
        # 对课程机构进行分页
        # 尝试获取前台get请求传递过来的page参数
        # 如果是不合法的配置参数默认返回第一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_orgs, 10, request=request)
        orgs = p.page(page)

        return render(request, "enter-list.html", {
            "all_orgs": orgs,
            # "enter": enter,
            "org_nums": org_nums,
            'reg':reg,
            "category": category,
            'hot_orgs':hot_orgs,
            'sort':sort,
        })



class EnterHomeView(View):
    '''企业首页'''

    def get(self, request, enter_id):
        current_page = 'home'
        # 根据id找到课程机构
        enter_org = Base.objects.get(id=int(enter_id))
        know_enter = Knowledge.objects.all()
        mon_enter = Money_report.objects.all()
        year_enter = Year_report.objects.all()
        # course_org.click_nums += 1
        # course_org.save()

        all_know = know_enter.filter(enter_id=int(enter_id))
        all_money = mon_enter.filter(enter_id=int(enter_id))
        all_year = year_enter.filter(enter_id=int(enter_id))
        return render(request,'enter-detail-homepage.html',{
            'enter_org':enter_org,
            'all_know':all_know,
            'all_money':all_money,
            'current_page':current_page,
            'all_year':all_year,
        })


class ChartsView(View):
    '''企业画像分类'''
    def get(self, request):
        all_orgs = Base.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_orgs, 10, request=request)
        all_orgs = p.page(page)
        return render(request,'echarts_page.html',{
            "all_orgs": all_orgs,
        })



#图表
def echarts_data(request):
    #取企业基本信息表，计算每个行业的总数，并从大到小排列
    _x = Base.objects.values_list('industry').annotate(Count('id')).order_by('-id__count')[:20]

    #横坐标为行业名，纵坐标为数量
    jsondata = {
        "key": [i[0] for i in _x],
        "value": [i[1] for i in _x]
    }
    return JsonResponse(jsondata,json_dumps_params={'ensure_ascii':False})


def echarts_page(request):
    #取企业基本信息表，计算每个行业的总数，并从大到小排列
    _x = Base.objects.values_list('flag').annotate(Count('id')).order_by('-id__count')[:20]

    #横坐标为行业名，纵坐标为数量
    jsondata = {
        "flag": [i[0] for i in _x],
        "val": [i[1] for i in _x]
    }
    return JsonResponse(jsondata,json_dumps_params={'ensure_ascii':False})


def echarts_type(request):
    #取企业基本信息表，计算每个行业的总数，并从大到小排列
    _x = Base.objects.values_list('type').annotate(Count('id')).order_by('-id__count')[:20]

    #横坐标为行业名，纵坐标为数量
    jsondata = {
        "type": [i[0] for i in _x],
        "num": [i[1] for i in _x]
    }
    return JsonResponse(jsondata,json_dumps_params={'ensure_ascii':False})


def echarts_mape(request):
    #取企业基本信息表，计算每个行业的总数，并从大到小排列
    _x = Base.objects.values_list('region').annotate(Count('id')).order_by('-id__count')[:20]

    #横坐标为行业名，纵坐标为数量
    jsondata = {
        "reg": [i[0] for i in _x],
        "list": [i[1] for i in _x]
    }
    return JsonResponse(jsondata,json_dumps_params={'ensure_ascii':False})



class EnterHomeChartView(View):

    def get(self,request, enter_id):
      #知识产权柱状图
       know_enter = Knowledge.objects.all()
       _x = know_enter.filter(enter_id=int(enter_id)).values_list()

       # 横坐标为行业名，纵坐标为数量
       jsondata = {
           "key":   ['专利','商标','著作权' ],
           "value": [_x[0][2],_x[0][3],_x[0][4] ]
        }
       return JsonResponse(jsondata, json_dumps_params={'ensure_ascii': False})


#单个用户三年内(折线图)
class Per_YearsChartView(View):
    def get(self, request, enter_id):
        year_enter = Year_report.objects.all()
        _x = year_enter.filter(enter_id=int(enter_id)).values_list()
        print(_x)
        jsondata = {

              '资产总额': [_x[0][3], _x[1][3], _x[2][3]],
              '负债总额' :[_x[0][4], _x[1][4], _x[2][4]],
              '营业总收入':[_x[0][5], _x[1][5], _x[2][5]],
              '主营业务收入':[_x[0][6], _x[1][6], _x[2][6]],
              '利润总额':[_x[0][7], _x[1][7], _x[2][7]],
              '净利润':[_x[0][8], _x[1][8], _x[2][8]],
              '纳税总额':[_x[0][9], _x[1][9], _x[2][9]],
              '所有者权益合计': [_x[0][10],_x[1][10],_x[2][10]],
        }
        print('jsondata',jsondata)
        return JsonResponse(jsondata, json_dumps_params={'ensure_ascii': False})



#单个企业2015年数据
class PerYear_2015_ChartView(View):
    def get(self,request, enter_id):
       year_enter = Year_report.objects.all()
       _x = year_enter.filter(enter_id=int(enter_id)).values_list()

       # 横坐标为行业名，纵坐标为数量
       jsondata = {
           "key":    [ '资产总额','负债总额','营业总收入','主营业务收入','利润总额','净利润','纳税总额','所有者权益合计'],
           "value": [_x[0][3],_x[0][4],_x[0][5],_x[0][6],_x[0][7],_x[0][8],_x[0][9],_x[0][10] ]
        }
       return JsonResponse(jsondata, json_dumps_params={'ensure_ascii': False})


class PerYear_2016_ChartView(View):
    def get(self,request, enter_id):
       year_enter = Year_report.objects.all()
       _x = year_enter.filter(enter_id=int(enter_id)).values_list()

       # 横坐标为行业名，纵坐标为数量
       jsondata = {
           "key":    [ '资产总额','负债总额','营业总收入','主营业务收入','利润总额','净利润','纳税总额','所有者权益合计'],
           "value": [_x[1][3],_x[1][4],_x[1][5],_x[1][6],_x[1][7],_x[1][8],_x[1][9],_x[1][10] ]
        }
       return JsonResponse(jsondata, json_dumps_params={'ensure_ascii': False})


class PerYear_2017_ChartView(View):
    def get(self,request, enter_id):
       year_enter = Year_report.objects.all()
       _x = year_enter.filter(enter_id=int(enter_id)).values_list()

       # 横坐标为行业名，纵坐标为数量
       jsondata = {
           "key":    [ '资产总额','负债总额','营业总收入','主营业务收入','利润总额','净利润','纳税总额','所有者权益合计'],
           "value": [_x[2][3],_x[2][4],_x[2][5],_x[2][6],_x[2][7],_x[2][8],_x[2][9],_x[2][10] ]
        }
       return JsonResponse(jsondata, json_dumps_params={'ensure_ascii': False})
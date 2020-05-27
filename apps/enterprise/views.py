from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from enterprise.models import Base, RegionDict
from django.db.models import Q

class EnterView(View):
    '''课程机构'''

    def get(self, request):
        # 所有企业
        all_orgs = Base.objects.all()

        # 所有金融报表
        all_city = RegionDict.objects.all()

        # 机构搜索功能
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            # 在name字段进行操作,做like语句的操作。i代表不区分大小写
            # or操作使用Q
            all_orgs = all_orgs.filter(Q(enterprise_id__icontains=search_keywords) | Q(type__icontains=search_keywords))
        # 行业筛选
        industry_id = request.GET.get('industry','')
        if industry_id:
            all_orgs = all_orgs.filter(industry_id=int(industry_id))

        # 类别筛选
        category = request.GET.get('ct','')
        if category:
            all_orgs = all_orgs.filter(category=category)

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
        p = Paginator(all_orgs, 2, request=request)
        orgs = p.page(page)

        return render(request, "enter-list.html", {
            "all_orgs": orgs,
            "all_citys": all_city,
            "org_nums": org_nums,
            'industry':industry_id,
            "category": category,
            'hot_orgs':hot_orgs,
            'sort':sort,
        })



class EnterHomeView(View):
    '''企业首页'''

    def get(self, request, enter_id):
        current_page = 'home'
        # 根据id找到课程机构
        course_org = Base.objects.get(id=int(enter_id))
        course_org.click_nums += 1
        course_org.save()
        # 判断收藏状态
        # has_fav = False
        # if request.user.is_authenticated:
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
        #         has_fav = True
        # 反向查询到课程机构的所有课程和老师
        all_know = course_org.know_set.all()[:4]
        all_money = course_org.money_set.all()[:2]
        all_year = course_org.year_set.all()[:2]
        return render(request,'org-detail-homepage.html',{
            'course_org':course_org,
            'all_know':all_know,
            'all_money':all_money,
            'current_page':current_page,
            'all_year':all_year,
        })
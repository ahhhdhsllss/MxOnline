# organization/urls.py

# from organization.views import OrgView,AddUserAskView
#
# from django.urls import path,re_path
# from .views import OrgHomeView,OrgCourseView,OrgDescView,OrgTeacherView,AddFavView
# from .views import TeacherListView,TeacherDetailView
#
# # 要写上app的名字
# app_name = "organization"
#
# urlpatterns = [
#     path('list/',OrgView.as_view(),name='org_list'),
#     path('add_ask/', AddUserAskView.as_view(), name="add_ask"),
#     re_path('home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name="org_home"),
#     re_path('course/(?P<org_id>\d+)/', OrgCourseView.as_view(), name="org_course"),
#     re_path('desc/(?P<org_id>\d+)/', OrgDescView.as_view(), name="org_desc"),
#     re_path('org_teacher/(?P<org_id>\d+)/', OrgTeacherView.as_view(), name="org_teacher"),
#
#     # 机构收藏
#     path('add_fav/', AddFavView.as_view(), name="add_fav"),
#     # 讲师列表
#     path('teacher/list/', TeacherListView.as_view(), name="teacher_list"),
#     # 讲师详情
#     re_path('teacher/detail/(?P<teacher_id>\d+)/', TeacherDetailView.as_view(), name="teacher_detail"),
#
# ]
from django.views.generic import TemplateView
import xadmin
from django.urls import path,re_path
from enterprise.views import EnterView, EnterHomeView, EnterHomeChartView, \
    Per_YearsChartView, PerYear_2015_ChartView, PerYear_2016_ChartView, PerYear_2017_ChartView

# 要写上app的名字
from xadmin.plugins.chart import ChartsView

app_name = "enterprise"
urlpatterns = [
    # path('list/', xadmin.site.urls),
    path('list/', EnterView.as_view(), name='enter_list'),
    re_path('home/(?P<enter_id>\d+)/info', EnterHomeView.as_view(), name="enter_home"),
    #获取单个企业知识产权数据
    re_path('home/(?P<enter_id>\d+)/perecharts', TemplateView.as_view(template_name='perecharts.html'), name='perecharts'),
    re_path('home/(?P<enter_id>\d+)/api/perecharts',EnterHomeChartView.as_view(), name='perecharts-url'),

    #单个企业三年年报数据(折线图)
    re_path('home/(?P<enter_id>\d+)/api/per_years_charts_years',Per_YearsChartView.as_view(), name='perecharts-url_years'),

    #单个企业2015年年报数据
    re_path('home/(?P<enter_id>\d+)/api/per_ayear_2015_echarts',PerYear_2015_ChartView.as_view(), name='per_ayear_2015_echarts-url_peryear'),
    # 单个企业2016年年报数据
    re_path('home/(?P<enter_id>\d+)/api/per_ayear_2016_echarts', PerYear_2016_ChartView.as_view(),
            name='per_ayear_2016_echarts-url_peryear'),
    # 单个企业2017年报数据
    re_path('home/(?P<enter_id>\d+)/api/per_ayear_2017_echarts', PerYear_2017_ChartView.as_view(),
            name='per_ayear_2017_echarts-url_peryear'),


    path('charts/', ChartsView.as_view(), name='enter_charts'),

     #测试折线图，未实现
    re_path('home/(?P<enter_id>\d+)/over_chart', TemplateView.as_view(template_name='over_chart.html'),
         name='over_chart'),
    re_path('home/(?P<enter_id>\d+)/api/over_chart',Per_YearsChartView.as_view(), name='over_chart-url_years'),

]
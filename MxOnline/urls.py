

# MxOnline/urls.py

import xadmin

from django.urls import path,include,re_path

from django.views.generic import TemplateView
from users.views import LoginView, RegisterView, ActiveUserView, ResetView, ModifyPwdView
from users.views import ForgetPwdView
from enterprise.views import EnterView


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
#    path('chart/',views.chart),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',LoginView.as_view(),name = 'login'),
    path('register/',RegisterView.as_view(),name = 'register'),
    path('captcha/',include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    path("users/", include('users.urls', namespace="users")),

    # 企业APP相关url配置
    path("enter/", include('enterprise.urls', namespace="enterprise")),
    path("org/", include('organization.urls', namespace="org")),
    # path("enter_list/", include(EnterView.as_view(),name = 'enter_list')),
]
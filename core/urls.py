from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    url(r'^$',views.home, name = "home"),
    url(r'login/', views.login_user, name = 'login'),
    url(r'^logout/$', views.logout_user, name= "logout"),

    #----------------------------------------------------------------------------
    url(r'^profile/(?P<user_name>\w+)/$', views.profile_user, name= "profile"),
    #---------------------------------------------------------------------------
    url(r'^register/$', views.register_user, name= "register"),
    url(r'^edit_profile/$', views.edit_profile, name = "edit_profile"),
    url(r'^dashbaord/$', views.dashboard, name = "dashboard"),
    
    #Password Change URL............
    url(r'^change_password/$', views.change_password, name = "change_password"),

    #password Reset URLS...........
    path('password_reset/', PasswordResetView.as_view(), name='password_reset' ),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #Email Confirm URLs.....
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),

    #Contact Us Page ...
    url(r'^contact/$', views.contact, name="contact"),
    #level 1 urls
    url(r'^list/$', views.BlogList, name="list"),
    url(r'^docview/$', views.docview, name="doccreate"),
    url(r'^detail/(?P<slug>[-\w]+)/$',views.BlogDetail,name='detail'),
    url(r'^completeArticle/(?P<slug>[-\w]+)/$',views.completeArticle,name='completeArticle'),
    url(r'^ParentCategoryview/$', views.ParentCategoryview, name="ParentCategoryview"),
    url(r'^Categoryview/$', views.Categoryview, name="Categoryview"),
    url(r'^categorylist/$', views.categorylist, name="categorylist"),
    url(r'^articlelist/$', views.articlelist, name="articlelist"),
    #Edit urls
    url(r'^editdocs/(?P<id>\d+)/$', views.DocEditView, name="DocEditView"),
    url(r'^CategoryEditView/(?P<id>\d+)/$', views.CategoryEditView, name="CategoryEditView"),
    url(r'^ParentCategoryEditView/(?P<id>\d+)/$', views.ParentCategoryEditView, name="ParentCategoryEditView"),


]

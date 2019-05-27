from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register_user'),
    #url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileView.as_view(), name='profileview'),

]


from django.conf.urls import url
from . import views # since view is already in teh current directory so...



urlpatterns = [
    url(r'^$',views.neu_mscs_List),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail),
]

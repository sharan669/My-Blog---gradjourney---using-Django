
from django.conf.urls import url
from . import views # since view is already in teh current directory so...

app_name = 'neuMSCS'

urlpatterns = [
    url(r'^$',views.neu_mscs_List, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]

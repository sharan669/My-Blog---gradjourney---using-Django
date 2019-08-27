
from django.contrib import admin
from django.conf.urls import url, include
from . import views # since view is already in teh current directory so...



urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^neumscs/$',include('neuMSCS.urls')),
    url(r'^about/$',views.about),
    url(r'^$',views.homepage),
]

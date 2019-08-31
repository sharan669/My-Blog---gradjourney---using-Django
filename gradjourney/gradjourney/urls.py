
from django.contrib import admin
from django.conf.urls import url, include
from . import views # since view is already in teh current directory so...
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from neuMSCS import views as neuMSCS_views


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^neumscs/',include('neuMSCS.urls')),
    url(r'^about/$',views.about),
    url(r'^$',neuMSCS_views.neu_mscs_List,name="home"),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

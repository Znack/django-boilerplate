from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^docs/', include('rest_framework_swagger.urls')),

]

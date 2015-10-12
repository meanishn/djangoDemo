from django.conf.urls import patterns, include, url
from django.contrib import admin
from demo import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/$', views.index, name="index"),
    url(r'^admin/', include(admin.site.urls)),
)

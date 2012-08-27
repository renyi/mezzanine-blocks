from django.conf.urls.defaults import patterns, url
from django.contrib.admin.views.decorators import staff_member_required
from views import edit

urlpatterns = patterns('',
    url(r'^edit/(?P<pk>\d+)/$', staff_member_required(edit), name='blocks-edit')
)

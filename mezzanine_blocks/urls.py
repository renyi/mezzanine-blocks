from django.conf.urls import re_path
from django.contrib.admin.views.decorators import staff_member_required
from views import edit

urlpatterns = [
    re_path(
        r"^edit/(?P<pk>\d+)/$",
        staff_member_required(edit),
        name="blocks-edit",
    ),
]

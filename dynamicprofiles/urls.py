from django.conf.urls import url

from dynamicprofiles.views import ProfileListView

urlpatterns = [
    url(r'^$', ProfileListView.as_view(), name="profile_list"),
]

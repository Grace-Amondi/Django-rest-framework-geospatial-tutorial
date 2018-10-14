from django.conf.urls import url, include
from .views import UserViewSet, GroupViewSet, SchoolViewSet, api_root
from rest_framework.urlpatterns import format_suffix_patterns

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy'
})

group_list = GroupViewSet.as_view({
    'get': 'list'
})
group_detail = GroupViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy'
})

school_list = SchoolViewSet.as_view({
    'get': 'list'
})
school_detail = SchoolViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy'
})
urlpatterns = [
    url(r'^$', api_root),
    url(r'^users', user_list, name=user_list),
    url(r'^user/(?P<pk>[0-9]+)/$', user_detail, name=user_detail),
    url(r'^groups', user_list, name=group_list),
    url(r'^groups/(?P<pk>[0-9]+)/$', user_detail, name=group_detail),
    url(r'^schools', school_list, name=school_list),
    url(r'^schools/(?P<pk>[0-9]+)/$', school_detail, name=school_detail),
]  # Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

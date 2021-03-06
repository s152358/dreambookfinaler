from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^accounts/register/$', views.register_page, name='register_page'),
    url(r'^api/$', views.PostsList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.PostsDetail.as_view()),
    url(r'^accounts/profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile'),
    url(r'^post/(?P<pk>\d+)/up/$', views.dream_vote, name='dream_vote'),
    url(r'^post/(?P<pk>\d+)/down/$', views.nightmare_vote, name='nightmare_vote'),

]
urlpatterns = format_suffix_patterns(urlpatterns)

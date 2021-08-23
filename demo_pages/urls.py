from django.conf.urls import include,url
from demo_pages import views


urlpatterns=[
    url(r'^test/$',views.test),
    url(r'^test2/$',views.TestView.as_view()),
    url(r'^$',views.index),
    url(r'^index2/$',views.IndexPageView.as_view()),
    url(r'^page2/$',views.page2)
]


from django.conf.urls import include,url
from demo_pages import views


urlpatterns=[
    url(r'^test/$',views.test),
    url(r'^$',views.index),
    url(r'^page2/$',views.page2)
]


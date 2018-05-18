
from django.conf.urls import url
from sample import views

urlpatterns = [
    url(r'^messagelist/$', views.MessageList.as_view(), name='message_list'),
    url(r'^addmessage/$', views.add_message, name='add_message'),
    url(r'^delete/message/(?P<id>[0-9]+)/$', views.delete_message, name='delete_message'),
    url(r'^edit/message/$', views.edit_message, name='edit_message'),

]
from django.urls import path
from .views import AnnounceList,AnnounceDetail, reply_to_announce

app_name = 'announces'

urlpatterns = [
    path('', AnnounceList.as_view(), name='announces'),
    path('<int:pk>', AnnounceDetail.as_view(), name='announce_detail'),
    path('reply/<int:pk>', reply_to_announce, name='reply_to_announce')
]
from django.urls import path
from christmas.views import (
    members_view,
    wishes_view,
    wish_view,
    comment_view
)


urlpatterns = [
    path("<group_name>/members/", members_view),
    path("<group_name>/wishes/<uuid:identifier>/", wishes_view),
    path("<group_name>/wish/<uuid:identifier>/", wish_view),
    path("<group_name>/wish/", wish_view),
    path("<group_name>/comment/", comment_view),
]

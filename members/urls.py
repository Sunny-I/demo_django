from django.urls import path
from members.views import show_members,member_detail

urlpatterns = [
    path('members/',show_members, name = "all-members"),
    path('members/detail/<int:id>/',member_detail,name = "detail-member")
]
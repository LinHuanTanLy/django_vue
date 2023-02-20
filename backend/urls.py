from backend.views import query_all_link
from django.urls import path,include

urlpatterns = [

    path("queryAllLinks", query_all_link)
]

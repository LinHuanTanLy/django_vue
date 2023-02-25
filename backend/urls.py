from backend.views import query_all_link, add_link, delete_link
from django.urls import path, include

urlpatterns = [

    path("queryAllLinks", query_all_link),
    path("addLink", add_link),
    path("deleteLink", delete_link)
]

from . import views 
from django.urls import path



urlpatterns = [
    path("homepage/",views.homepage,name="posts_home"),
    # path("",views.list_posts,name="list_posts"),   '''without using class based views'''
    path("",views.PostListCreateView.as_view(),name="list_create_posts"),  # using class based views
    # path("<int:post_index>/",views.post_detail,name="post_detail"),
    # path("update/<int:post_index>/",views.update_post,name="update_post"),
    # path("delete/<int:post_index>/",views.delete_post,name="delete_post"),
    path("<int:pk>/",views.PostRetrieveUpdateDeleteView.as_view(),name="post_rud"),  # using class based views
]


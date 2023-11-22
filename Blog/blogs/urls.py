from django.urls import path
from . import views

app_name="blogs"

urlpatterns = [

    path("add/" , views.add_blogs_view, name="add_blogs_view"),
    path("", views.show_blogs_view, name="show_blogs_view"),
    path("detail/<blog_id>/",views.blog_detail_view, name ="blog_detail_view"),
    path("not_found/",views.not_found_view, name="not_found_view")
    
]
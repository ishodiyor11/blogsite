from django.urls import path
from .views import user_page, blog_page, comment_page, tlogcomment_page

urlpatterns = [
    
    path("", blog_page, name='blog'),
    path("comment/", comment_page, name='comment'),
    path("tlogcomment/", tlogcomment_page, name='tlogcomment'),
    path("users/", user_page, name='user')

]

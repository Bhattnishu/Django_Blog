from django.urls import path
from . import views


urlpatterns = [

    # Category
    path(
        'category/<int:category_id>/',
        views.posts_by_category,
        name='posts_by_category'
    ),

    # Comment
    path(
        'comments/edit/<int:pk>/',
        views.edit_comment,
        name='edit_comment'
    ),

    path(
        'comments/delete/<int:pk>/',
        views.delete_comment,
        name='delete_comment'
    ),

]

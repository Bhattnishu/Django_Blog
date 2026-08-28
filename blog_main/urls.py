"""
URL configuration for blog_main project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from blogs import views as BlogsView


urlpatterns = [

    # Admin
    path(
        "admin/",
        admin.site.urls
    ),

    # Home
    path(
        "",
        views.home,
        name='home'
    ),

    # Categories
    path(
        "category/",
        include('blogs.urls')
    ),

    # Blog detail
    path(
        "blogs/<slug:slug>/",
        BlogsView.blogs,
        name='blogs'
    ),

    # Search
    path(
        "search/",
        BlogsView.search,
        name='search'
    ),

    # Authentication
    path(
        "register/",
        views.register,
        name='register'
    ),

    path(
        "login/",
        views.login,
        name='login'
    ),

    path(
        "logout/",
        views.logout,
        name='logout'
    ),

    # Comment
    path(
        "comments/edit/<int:pk>/",
        BlogsView.edit_comment,
        name='edit_comment'
    ),

    path(
        "comments/delete/<int:pk>/",
        BlogsView.delete_comment,
        name='delete_comment'
    ),

    # Dashboard
    path(
        "dashboard/",
        include('dashboard.urls')
    ),

] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
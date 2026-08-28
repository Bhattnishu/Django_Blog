from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category, Comment
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Posts by Category
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(
        status='Published',
        category=category_id
    )

    category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category': category,
    }

    return render(request, 'posts_by_category.html', context)


# Single Blog
def blogs(request, slug):
    single_blog = get_object_or_404(
        Blog,
        slug=slug,
        status="Published"
    )

    # Add comment
    if request.method == 'POST':

        if not request.user.is_authenticated:
            return redirect('login')

        comment_text = request.POST.get('comment', '').strip()

        if comment_text:
            comment = Comment()
            comment.user = request.user
            comment.blog = single_blog
            comment.comment = comment_text
            comment.save()

        return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(
        blog=single_blog
    ).order_by('-created_at')

    comment_count = comments.count()

    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,
    }

    return render(request, 'blogs.html', context)


# Edit Comment
@login_required(login_url='login')
def edit_comment(request, pk):

    # Only the owner of the comment can edit it
    comment = get_object_or_404(
        Comment,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':

        comment_text = request.POST.get('comment', '').strip()

        if comment_text:
            comment.comment = comment_text
            comment.save()

        return redirect(
            'blogs',
            slug=comment.blog.slug
        )

    context = {
        'comment': comment,
    }

    return render(
        request,
        'edit_comment.html',
        context
    )


# Delete Comment
@login_required(login_url='login')
def delete_comment(request, pk):

    # Only the owner of the comment can delete it
    comment = get_object_or_404(
        Comment,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':

        blog_slug = comment.blog.slug

        comment.delete()

        return redirect(
            'blogs',
            slug=blog_slug
        )

    return redirect(
        'blogs',
        slug=comment.blog.slug
    )


# Search
def search(request):

    keyword = request.GET.get('keyword', '').strip()

    if keyword:
        blogs = Blog.objects.filter(
            Q(title__icontains=keyword) |
            Q(short_description__icontains=keyword) |
            Q(blog_body__icontains=keyword),
            status='Published'
        )
    else:
        blogs = Blog.objects.filter(
            status='Published'
        )

    context = {
        'blogs': blogs,
        'keyword': keyword,
    }

    return render(request, 'search.html', context)

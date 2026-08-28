from django.shortcuts import get_object_or_404, render, redirect
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import AddUserForm, BlogPostForm, CategoryForm, EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Staff check
def staff_only(user):
    return user.is_authenticated and user.is_staff


# Dashboard
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()

    context = {
        'category_count': category_count,
        'blog_count': blog_count,
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )


# Categories
@login_required(login_url='login')
def categories(request):
    categories = Category.objects.all().order_by('-created_at')

    context = {
        'categories': categories,
    }

    return render(
        request,
        'dashboard/categories.html',
        context
    )


@login_required(login_url='login')
def add_category(request):

    if request.method == "POST":

        form = CategoryForm(request.POST)

        if form.is_valid():

            category = form.save(commit=False)

            # Logged-in user owns the category
            category.created_by = request.user

            category.save()

            return redirect('categories')

    else:

        form = CategoryForm()

    context = {
        'form': form,
    }

    return render(
        request,
        'dashboard/add_category.html',
        context
    )


@login_required(login_url='login')
def edit_category(request, pk):

    # Only category owner can edit
    category = get_object_or_404(
        Category,
        pk=pk,
        created_by=request.user
    )

    if request.method == "POST":

        form = CategoryForm(
            request.POST,
            instance=category
        )

        if form.is_valid():

            form.save()

            return redirect('categories')

    else:

        form = CategoryForm(instance=category)

    context = {
        'form': form,
        'category': category,
    }

    return render(
        request,
        'dashboard/edit_category.html',
        context
    )


@login_required(login_url='login')
def delete_category(request, pk):

    # Only category owner can delete
    category = get_object_or_404(
        Category,
        pk=pk,
        created_by=request.user
    )

    if request.method == "POST":

        category.delete()

        return redirect('categories')

    return redirect('categories')


# Posts
@login_required(login_url='login')
def posts(request):

    posts = Blog.objects.all().order_by('-created_at')

    context = {
        'posts': posts,
    }

    return render(
        request,
        'dashboard/posts.html',
        context
    )


@login_required(login_url='login')
def add_post(request):

    if request.method == "POST":

        form = BlogPostForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            post = form.save(commit=False)

            # Logged-in user owns the post
            post.author = request.user

            post.save()

            title = form.cleaned_data['title']

            post.slug = slugify(title) + '-' + str(post.id)

            post.save()

            return redirect('posts')

    else:

        form = BlogPostForm()

    context = {
        'form': form,
    }

    return render(
        request,
        'dashboard/add_post.html',
        context
    )


@login_required(login_url='login')
def edit_post(request, pk):

    # Only post owner can edit
    post = get_object_or_404(
        Blog,
        pk=pk,
        author=request.user
    )

    if request.method == "POST":

        form = BlogPostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():

            post = form.save()

            title = form.cleaned_data['title']

            post.slug = slugify(title) + '-' + str(post.id)

            post.save()

            return redirect('posts')

    else:

        form = BlogPostForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(
        request,
        'dashboard/edit_post.html',
        context
    )


@login_required(login_url='login')
def delete_post(request, pk):

    # Only post owner can delete
    post = get_object_or_404(
        Blog,
        pk=pk,
        author=request.user
    )

    if request.method == "POST":

        post.delete()

        return redirect('posts')

    return redirect('posts')


# Users
# Only staff users can access these views

@user_passes_test(staff_only, login_url='login')
def users(request):

    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(
        request,
        'dashboard/users.html',
        context
    )


@user_passes_test(staff_only, login_url='login')
def add_user(request):

    if request.method == "POST":

        form = AddUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('users')

    else:

        form = AddUserForm()

    context = {
        'form': form,
    }

    return render(
        request,
        'dashboard/add_user.html',
        context
    )


@user_passes_test(staff_only, login_url='login')
def edit_user(request, pk):

    user = get_object_or_404(
        User,
        pk=pk
    )

    if request.method == 'POST':

        form = EditUserForm(
            request.POST,
            instance=user
        )

        if form.is_valid():

            form.save()

            return redirect('users')

    else:

        form = EditUserForm(
            instance=user
        )

    context = {
        'form': form,
    }

    return render(
        request,
        'dashboard/edit_user.html',
        context
    )


@user_passes_test(staff_only, login_url='login')
def delete_user(request, pk):

    user = get_object_or_404(
        User,
        pk=pk
    )

    if request.method == "POST":

        user.delete()

        return redirect('users')

    return redirect('users')
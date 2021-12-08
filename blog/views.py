
from django.contrib.auth import login, authenticate
from django.forms.forms import Form 
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from .models import Post
from .models import Comment
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import *
from .models import *
from django.shortcuts import redirect
from .forms import RegistrationForm, CommentForm
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    paginator = Paginator(posts, 4)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'posts': posts, 'page': page })


def profile(request):
    if request.user.is_authenticated:
        user_posts = Post.objects.filter(author=request.user)
        liked_posts = Post.objects.filter(likes=request.user)
        return render(request, 'user_files/profile.html', {'user_posts': user_posts, 'liked_posts': liked_posts})
    else:
        return redirect('login')
    


def hello(request):
    return render(request, 'blog/hello.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    total_likes = post.total_likes()
    latest_comments_list = Comment.objects.filter(post=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.post = post
            form.save()
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'latest_comments_list': latest_comments_list,
                                                     'form': form, 'total_likes': total_likes})


def best_post(request, pk):
    best_post = Post.objects.annotate(num_likes=Post.total_likes()).filter(num_likes__gt=70).order_by('-created_date')
    b_post = get_object_or_404(best_post, pk=pk)
    total_likes = b_post.total_likes()
    latest_comments_list = Comment.objects.filter(post=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.post = b_post
            form.save()
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'best_post': best_post, 'b_post': b_post, 'latest_comments_list': latest_comments_list, 'total_likes': total_likes,
                'form': form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = RegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def leave_comment(request, post_id):
    p_id = Post.objects.get(id=post_id)
    p_id.comment_set.create(author_name=request.user, comment_text=request.post['TEXT'])


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


def login_user(request):
    if request.method == 'POST':
        login_form = LoginUserForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                return HttpResponseRedirect("?next=/main_menu/")
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginUserForm()
    return render(request, 'registration/login.html', {'login_form': login_form})


def category_view(request, cats):
    category_posts = Post.objects.filter(category=cats)
    paginator = Paginator(category_posts, 4)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        category_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        category_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        category_posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/categories.html', {'cats': cats.title(), 'category_posts': category_posts, 'page': page})


def main_menu(request):
   # pubg = Post.objects.filter(id=1) #Pubg
   # minecraft = Post.objects.filter(id=2) #minecraft
    #dota = Post.objects.filter(id=6) #dota
    #wot = Post.objects.filter(id=5) #wot
   # gta = Post.objects.filter(id=11) #gta
   # csgo = Post.objects.filter(id=7) #csgo
    
    post_categoryes = choice_list
    return render(request, 'blog/main_menu.html', {
        'post_categoryes': post_categoryes, 
       # 'pubg': pubg, 
       #'minecraft': minecraft, 
       # 'wot': wot, 
       # 'dota': dota,
        #'csgo': csgo,
       # 'gta': gta })
    })


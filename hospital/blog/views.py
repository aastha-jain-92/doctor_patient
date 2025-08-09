# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm

@login_required
def doctor_create_post(request):
    if request.user.user_type != 'doctor':
        import pdb; pdb.set_trace()
        return redirect('blog:post_list')  # redirect patients away

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:doctor_posts')
    else:
        form = BlogPostForm()
    return render(request, 'doctor_create_post.html', {'form': form})

@login_required
def doctor_posts(request):
    if request.user.user_type != 'doctor':
        return redirect('blog:post_list')
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'doctor_posts.html', {'posts': posts})

def post_list_by_category(request, category=None):
    categories = dict(BlogPost.CATEGORY_CHOICES)  # {'Mental Health':..., ...}
    posts = BlogPost.objects.filter(is_draft=False)
    if category:
        posts = posts.filter(category=category)
    return render(request, 'post_list.html', {
        'categories': categories,
        'selected_category': category,
        'posts': posts
    })

def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if post.is_draft and (not request.user.is_authenticated or request.user != post.author):
        return redirect('post_list')
    return render(request, 'post_detail.html', {'post': post})

def patient_blogs(request):
    blogs_by_category = {}
    
    # Get all published (non-draft) posts
    posts = BlogPost.objects.filter(is_draft=False)

    for post in posts:
        category_name = post.category  # category is just a string field
        blogs_by_category.setdefault(category_name, []).append(post)

    return render(request, 'patient_blogs.html', {
        'blogs_by_category': blogs_by_category
    })

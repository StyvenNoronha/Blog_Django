from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
def index(request):
    posts = Post.objects.get_published()
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'blog/pages/index.html',{'page_obj':page_obj})

def author(request, author_id):
    posts = Post.objects.get_published().filter(created_by__pk=author_id)
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'blog/pages/index.html',{'page_obj':page_obj})

def category(request, slug):
    posts = Post.objects.get_published().filter(category__slug=slug)
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'blog/pages/index.html',{'page_obj':page_obj})

def tag(request, slug):
    posts = Post.objects.get_published().filter(tags__slug=slug)
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'blog/pages/index.html',{'page_obj':page_obj})

def page(request, slug):
    return render(request,'blog/pages/page.html')

def post(request, slug):

    post = Post.objects.get_published().filter(slug=slug).first()

    return render(request,'blog/pages/post.html',{'post':post})

def search(request):
    search_value = request.GET.get('search','').strip()
    posts = Post.objects.get_published().filter(Q(title__icontains=search_value) | Q(excerpt__icontains=search_value) | Q(content__icontains=search_value))[:9]
    return render(request,'blog/pages/index.html',{'page_obj':posts,'search_value':search_value})
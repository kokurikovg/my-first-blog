from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
  posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  # requestはインターネットのを介してユーザから受け取った全ての情報
  # 'posts'は名前,postsはクエリセット(上記の変数)
  return render(request,'blog/post_list.html',{'posts':posts})


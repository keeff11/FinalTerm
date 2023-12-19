from django.shortcuts import render
from .models import Post  # Post 모델을 import
from rest_framework import viewsets
from .serializers import PostSerializer
from django.http import JsonResponse

def post_list(request):
    posts = Post.objects.all()  # Post 모델에서 모든 객체들을 가져옴
    return render(request, 'blog/post_list.html', {'posts': posts})  # 'posts' 변수를 포함하여 템플릿에 전달

def post_list2(request):
    # Post 모델에서 최신 객체(가장 최근 생성일을 기준으로) 하나만 가져옴
    posts = Post.objects.order_by('created_date').first()
    return render(request, 'blog/post_list2.html', {'posts': posts})
    
class IntruderImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def abc_view(request):
    image_url = "http://127.0.0.1:8000/media/intruder_image/2023/10/29/Coffee-Shop.png"
    data = {'image_url': image_url}
    return JsonResponse(data)
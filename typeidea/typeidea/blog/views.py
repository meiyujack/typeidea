from django.shortcuts import render
from django.http import HttpResponse

from .models import Post,Tag


def post_list(request,category_id=None,tag_id=None):
    
    if tag_id:
        try:
            tag_qs=Tag.get_all()
            tag=tag_qs.filter(id=tag_id)
        except Tag.DoesNotExist:
            post_list=[]
        else:
            post_list=tag.post_set.filter(status=Post.STATUS_NORMAL)
    else:
        post_list=Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            post_list=post_list.filter(category_id=category_id)
    return render(request,'blog/list.html',context={'post_list':post_list})


def post_detail(request,post_id=None):
    try:
        post_qs=Post.get_all()
        post=post_qs.filter(id=post_id)
    except Post.DoesNotExist:
        post=None
    return render(request,'blog/detail.html',context={'post':post})


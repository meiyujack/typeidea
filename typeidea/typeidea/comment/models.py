from django.db import models

from blog.models import Post


class Comment(models.Model):

    class Meta:
        verbose_name=verbose_name_plural="评论"
    
    STATUS_NORMAL=1
    STATUS_DELETE=0
    STATUS_ITEMS=(
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除')
    )
    post=models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name="评论文章",default=1)
    content=models.CharField(max_length=2000,verbose_name="内容")
    nickname=models.CharField(max_length=50,verbose_name="昵称")
    website=models.URLField(verbose_name="网站")
    email=models.EmailField(verbose_name="邮箱")
    status=models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    created_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    def __str__(self):
        return f"{self.content} on {self.post}"


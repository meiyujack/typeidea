from django.db import models

from django.contrib.auth.models import User

from typeidea.base_models import BaseModel


class Link(BaseModel):
    class Meta:
        verbose_name=verbose_name_plural="友链"

    STATUS_NORMAL=1
    STATUS_DELETE=0
    STATUS_ITEMS=(
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    title=models.CharField(max_length=50,verbose_name="标题")
    href=models.URLField(verbose_name="链接")  #默认长度为200
    status=models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    weight=models.PositiveIntegerField(default=1,choices=zip(range(1,6),range(1,6)),verbose_name="权重",help_text="权重高展示顺序靠前")
    owner=models.ForeignKey(User,verbose_name="作者",on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    def __str__(self):
        return self.title


class SideBar(BaseModel):

    class Meta:
        verbose_name=verbose_name_plural="侧边栏"

    STATUS_SHOW=1
    STATUS_HIDE=0
    STATUS_ITEMS=(
        (STATUS_SHOW,'展示'),
        (STATUS_HIDE,'隐藏'),
    )
    BROWSE_OPTIONS=(
        (1,'HTML'),
        (2,'最新文章'),
        (3,'最热文章'),
        (4,'最近评论'),
    )
    title=models.CharField(max_length=50,verbose_name="标题")
    browse_options=models.PositiveIntegerField(default=1,choices=BROWSE_OPTIONS,verbose_name="查看选项")
    content=models.CharField(max_length=500,blank=True,verbose_name="内容",help_text="如果设置的不是HTML类型,k 可为空")
    status=models.PositiveIntegerField(default=STATUS_SHOW,choices=STATUS_ITEMS,verbose_name="状态")
    owner=models.ForeignKey(User,verbose_name="作者",on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    def __str__(self):
        return self.title


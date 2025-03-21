from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry

from .models import Post,Category,Tag
from .adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin


class PostInline(admin.TabularInline):  # 可选择继承自admin.StackedInline,以获取不同的展示样式

    fields=('title','description')
    extra=1  # 控制额外多几个
    model=Post


@admin.register(Category,site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines=[PostInline,]
    list_display=('name','status','is_nav','created_time','post_count')
    fields=('name','status','is_nav')
    
    def post_count(self,obj):
        return obj.post_set.count()

    post_count.short_description="文章数量"


@admin.register(Tag,site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display=('name','status')
    fields=('name','status')
    
class CategoryOwnerFilter(admin.SimpleListFilter):
    """ 自定义过滤器只展示当前用户分类 """
    title='分类过滤器'
    parameter_name='owner_category'

    def lookups(self,request,model_admin):
        return Category.objects.filter(owner=request.user).values_list('id','name')
    

    def queryset(self,request,queryset):
        category_id=self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset


@admin.register(Post,site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form=PostAdminForm

    class Media:
        css={
            'all':("https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/5.3.3/css/bootstrap.min.css",),
        }
        js=("https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/5.3.3/js/bootstrap.bundle.js",)

    list_display=['title','category','status','created_time','operate']
    list_display_links=[]

    list_filter=[CategoryOwnerFilter]
    search_fields=['title','category__name']

    actions_on_top=True
    actions_on_bottom=True

    # 编辑页面
    save_on_top=True

    # fields=(('category','title'),'description','status','content','tags')
    fieldsets=(('基础配置',{'description':'基础配置描述','fields':(('title','category'),'status',)}),
               ('内容',{'fields':('description','content')}),
               ('额外信息',{'classes':('collapse',),'fields':('tags',)})
               )
    
    # filter_vertical=('tag',)

    def operate(self,obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change',args=(obj.id,))
        )
    operate.short_description='操作'

    def save_model(self,request,obj,form,change):
        obj.owner=request.user
        return super(PostAdmin,self).save_model(request,obj,form,change)
    
    def get_queryset(self, request):
        qs=super(PostAdmin,self).get_queryset(request)
        return qs.filter(owner=request.user)
        

@admin.register(LogEntry,site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display=['object_repr','action_flag','user','change_message','action_time']
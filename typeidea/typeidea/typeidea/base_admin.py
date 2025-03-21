from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1. 用来自动补充文章、分类、侧边栏、友链这些Model的owner字段
    2. 用来针对queryset过滤当前用户的数据
    """
    def get_queryset(self,request):
        queryset = super(BaseOwnerAdmin, self).get_queryset(request)
        queryset = queryset.filter(owner=request.user)
        return queryset

    def save_model(self, request, obj, form, change):
        obj.owner=request.user
        return super(BaseOwnerAdmin,self).save_model(request, obj, form, change)
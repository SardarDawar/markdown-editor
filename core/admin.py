from django.contrib import admin
from .models import *

class profileAdmin(admin.ModelAdmin):
    list_display = ['user']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Name',)}


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Name',)}



class Parent_CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Name',)}

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Parent_Category',),'slug1':('title',)}


admin.site.register(profileModel, profileAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Parent_Category,Parent_CategoryAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Sub_Category,SubCategoryAdmin)
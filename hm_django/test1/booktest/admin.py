#-*- coding:utf-8 -*-
from django.contrib import admin
from  models import BookInfo
from  models import HeroInfo # 不然 NameError: name 'HeroInfo' is not defined

class HeroInfoline(admin.StackedInline):
    model = HeroInfo
    extra =3

    
class BookInfoAdmin(admin.ModelAdmin):
    list_display=['id','btitle','bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle ']
    list_per_page = 1
    fieldsets = [
        ('base',{'fields':['btitle']}),
        ('super',{'fields':['bpub_date']})
        ]
    inlines=[HeroInfoline]

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)


# Register your models here.

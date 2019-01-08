#-*- coding:utf-8 -*-
from django.db import models

class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)
class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField(db_column='pub_date')
    bread=models.IntegerField(default=0) 
    bcommet=models.IntegerField(null=False)
    isDelete=models.BooleanField(default=False)
    class Meta:
        db_table='bookinfo'
    books1=models.Manager()
    books2=BookInfoManager()
    def __init__(self):

        
class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField(default=True)
    hcontent=models.CharField(max_length=1000)
    isDelete=models.BooleanField(default=False)
    book=models.ForeignKey(BookInfo)
# Create your models here.

05 模型类看到过 03:40   要职@classmethod  于是跳回去 看 /home/evan/python/py2018/第2章 python核心编程/第1节.python核心编程/02.python高级2-生成器、闭包、装饰器/视频
# insert into bookinfo(btitle,pub_date,bread,bcommet,isDelete) values ('射雕英雄传','1980-5-1',12,34,0), ('天龙八部','1986-7-24',36,40,0), ('笑傲江湖','1995-12-24',20,80,0), ('雪山飞狐','1987-11-11',58,24,0) ;

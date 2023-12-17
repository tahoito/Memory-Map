from django.db import models
from django.utils import timezone#追加する
import uuid#追加する

class Todo(models.Model):
    time = models.DateField(verbose_name="作成日", default=timezone.now)
    memo = models.TextField(max_length=255)

    
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Diary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)#自動でつく
    date = models.DateField(verbose_name='日付', default=timezone.now)#日付
    title = models.CharField(verbose_name='タイトル', max_length=40)#日付のタイトル
    text = models.CharField(verbose_name='本文', max_length=200)#日付の本文
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)#作成日時
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)#編集日時
    tagname = models.CharField(verbose_name='タグ', max_length=40,null=True,blank=True)#タグを書くスペース
    tag = models.ManyToManyField(Tag)
    #relation = models.ManyToManyField('self', verbose_name='関連', blank=True, null=True)
    
    def __str__(self):
            return self.title

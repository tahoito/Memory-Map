from django.db import models
from django.utils import timezone#追加する
import uuid#追加する
from django.contrib.auth.models import User

class Todo(models.Model):
    time = models.DateField(verbose_name="作成日", default=timezone.now)
    memo = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Diary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)#自動でつく
    date = models.DateField(verbose_name='日付', default=timezone.now)#日付
    title = models.CharField(verbose_name='タイトル', max_length=255)#日付のタイトル
    text = models.TextField(verbose_name='本文',blank=True,null=True,max_length=1000)#日付の本文
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)#作成日時
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)#編集日時
    tagname = models.CharField(verbose_name='タグ', max_length=40,null=True,blank=True)#タグを書くスペース
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
            return self.title
    

class Image(models.Model):
    name = models.CharField(verbose_name='題名',max_length=40)
    image = models.ImageField(upload_to='img/upload')
    memo = models.TextField(verbose_name='メモ',max_length=60,null=True,blank=True)
    today = models.DateTimeField(verbose_name='作成日', default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
     
    def __str__(self):
            return self.name

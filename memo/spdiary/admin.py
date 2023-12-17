from django.contrib import admin
from .models import Diary
from .models import Todo
from .models import Tag

admin.site.register(Diary)
admin.site.register(Todo)
admin.site.register(Tag)



# Register your models here.

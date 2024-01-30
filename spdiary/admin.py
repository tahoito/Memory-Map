from django.contrib import admin
from .models import Diary
from .models import Todo
from .models import Tag
from .models import Image

admin.site.register(Diary)
admin.site.register(Todo)
admin.site.register(Tag)
admin.site.register(Image)





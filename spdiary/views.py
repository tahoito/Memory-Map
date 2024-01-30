from django.shortcuts import render
from .models import Todo,Image
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import DiaryForm
from .forms import TodoForm
from .models import Diary
from django.contrib.auth.mixins import LoginRequiredMixin#ログインしてない人は編集不可
from .models import Tag 
from django.shortcuts import redirect
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from .forms import ImageForm
from django.shortcuts import render, get_object_or_404



#Diary
class SignupPage(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('spdiary:login')
    template_name = 'registration/signup.html'#htmlに飛ぶ


class DiaryCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = 'diary/create.html'
    model = Diary
    fields = ('date','title','text','tagname')
    success_url = reverse_lazy('spdiary:list')#createが終わったらcompleteの方へ移動する


    def form_valid(self, form):
    # userのコード
        diary_object = form.save(commit=False)
        diary_object.user = self.request.user  
        #diary_object.save()

    # ハッシュタグ機能
        diary = Diary(
            title=form.cleaned_data["title"], text=form.cleaned_data["text"], tagname=form.cleaned_data["tagname"],
            user=self.request.user
        )
        diary.save()
        words = form.cleaned_data["tagname"].split()
        for word in words:
            if word[0] == "#":
                if Tag.objects.filter(name=word[1:]).exists():
                    tag = Tag.objects.get(name=word[1:])
                else:
                    tag = Tag.objects.create(name=word[1:])
                diary.tag.add(tag)

        return redirect('spdiary:list')


class DiaryListView(LoginRequiredMixin,generic.ListView):
    template_name = 'diary/list.html'
    model = Diary

    #ハッシュタグ機能 
    def get_queryset(self):
        tag = self.request.GET.get('tag')

        if tag and self.request.user.is_active:
            diary_list = Diary.objects.filter(
                tag__name__icontains=tag,user=self.request.user)
        elif not tag and self.request.user.is_active:
            diary_list = Diary.objects.filter(user=self.request.user).order_by('-date')
        else:
            diary_list = Diary.objects.none()    
        return diary_list
    


class DiaryDetailView(generic.DetailView):
    template_name = 'diary/detail.html'
    model = Diary    

class DiaryUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'diary/update.html'
    model = Diary
    fields = ('date','title','text','tagname')
    success_url = reverse_lazy('spdiary:list')

    def form_valid(self, form):
        diary = form.save(commit=False)#あえて保存しない
        #diary.created_at = timezone.now()#時間を上書きする
        diary.save()
        return super().form_valid(form)
    
class DiaryDeleteView(generic.DeleteView):
    template_name = 'diary/delete.html'
    model = Diary
    success_url = reverse_lazy('spdiary:list')  

#Image
class ImageCreateView(generic.CreateView):
    model = Image
    fields = ('name','image','memo')
    template_name = 'image/Image.html'
    success_url = reverse_lazy('spdiary:ImageList') 

    def index(request):
        params = {
            'title': '画像のアップロード',
            'upload_form': ImageForm(),
            'id': None,
        }
 
        if (request.method == 'POST'):
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                upload_image = form.save()
 
                params['id'] = upload_image.id
 
        return render(request, 'spdiary:ImageList.html', params)
    
    def form_valid(self, form):
        image_object = form.save(commit=False)
        image_object.user = self.request.user  
        image_object.save()
        return super().form_valid(form)
    

class ImageListView(generic.ListView):
    model = Image
    template_name = 'Image/ImageList.html'


    def get_queryset(self):
        query = self.request.GET.get('query')

        if query and self.request.user.is_active:
            image_list = Image.objects.filter(
                name__icontains=query,user=self.request.user)
        elif not query and self.request.user.is_active:
            image_list = Image.objects.filter(user=self.request.user).order_by('-id')
        else:
            image_list = Image.objects.none()    
        return image_list

    
class ImageDetailView(generic.DetailView):
    model = Image
    queryset = Image.objects.all()
    template_name = 'image/ImageDetail.html'  

    def preview(request, image_id=0):
 
        upload_image = get_object_or_404(Image, id=image_id)
 
        params = {
            'title': '画像の表示',
            'id': upload_image.id,
            'url': upload_image.image.url
        }
 
        return render(request, 'image/ImageDetail.html', params)
    
class ImageDeleteView(generic.DeleteView):
    model = Image
    template_name = 'image/ImageDelete.html'
    success_url = reverse_lazy('spdiary:ImageList')

#Todo
class ListPage(generic.ListView):
    model = Todo
    template_name = 'todo/ListPage.html'

    #user機能
    def get_queryset(self):
        query = self.request.GET.get('query')

        if query and self.request.user.is_active:
            todo_list = Todo.objects.filter(
                memo__icontains=query,user=self.request.user)
        elif not query and self.request.user.is_active:
            todo_list = Todo.objects.filter(user=self.request.user).order_by('-id')
        else:
            todo_list = Todo.objects.none()    
        return todo_list
    


class CreatePage(generic.CreateView):
    template_name = 'todo/CreatePage.html'
    form_class = TodoForm
    success_url = reverse_lazy('spdiary:ListPage')  

    #user機能
    def form_valid(self, form):
        todo_object = form.save(commit=False)
        todo_object.user = self.request.user  
        todo_object.save()
        return super().form_valid(form)



class UpdatePage(generic.UpdateView):
    model = Todo
    template_name = 'todo/UpdatePage.html'
    fields = ('time','memo')
    success_url = reverse_lazy('spdiary:ListPage')  

class DeletePage(generic.DeleteView):
    model = Todo
    template_name = 'todo/DeletePage.html'
    fields = ('time','memo')
    success_url = reverse_lazy('spdiary:ListPage')  

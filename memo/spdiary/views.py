from django.shortcuts import render
from .models import Todo
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import DiaryForm
from .forms import TodoForm
from .models import Diary
from django.contrib.auth.mixins import LoginRequiredMixin#ログインしてない人は編集不可
from .models import Tag
from django.shortcuts import redirect

#日記を書く
class DiaryApp(generic.ListView):
    model = Diary#diaryを指定している（models.pyより）
    template_name = 'index.html'

class SignupPage(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'#htmlに飛ぶ


class DiaryCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = 'create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('spdiary:create_complete')#createが終わったらcompleteの方へ移動する

    def form_valid(self, form):
        diary = Diary(
            title=form.cleaned_data["title"], text=form.cleaned_data["text"],tagname=form.cleaned_data["tagname"])
        diary.save()
        words = form.cleaned_data["tagname"].split()
        for word in words:
            if word[0] == "#":
                if Tag.objects.filter(name=word[1:]).exists():
                    tag = Tag.objects.get(name=word[1:])
                else:
                    tag = Tag.objects.create(name=word[1:])
                diary.tag.add(tag)
        return redirect('spdiary:create_complete')
    
#class TagView(generic.ListView):
    #model = Diary
    #template_name = 'spdiary:list'

    #def get_queryset(self):
        #tag = Tag.objects.get(name=self.kwargs['tag'])
        #queryset = Diary.objects.order_by('-id').filter(tag=tag)
        #return queryset

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['tag_key'] = self.kwargs['tag']
        #return context
    

class DiaryCreateCompleteView(generic.CreateView):
    template_name = 'create_complete.html'
    form_class = DiaryForm
    success_url = reverse_lazy('index')#completeしたらindex(ホーム画面)に戻る 


class DiaryListView(LoginRequiredMixin,generic.ListView):
    template_name = 'list.html'
    model = Diary#Diaryモデルを指定している
    def get_queryset(self):
        tag = self.request.GET.get('tag')

        if tag:
            list = Diary.objects.filter(
                tag__name__icontains=tag)
        else:
            list = Diary.objects.all()
        return list

class DiaryDetailView(generic.DetailView):
    template_name = 'detail.html'
    model = Diary    

class DiaryUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'update.html'
    model = Diary
    fields = ('date','title','text')
    success_url = reverse_lazy('spdiary:list')

    def form_valid(self, form):
        diary = form.save(commit=False)#あえて保存しない
        #diary.created_at = timezone.now()#時間を上書きする
        diary.save()
        return super().form_valid(form)
    
class DiaryDeleteView(generic.DeleteView):
    template_name = 'delete.html'
    model = Diary
    success_url = reverse_lazy('spdiary:list')  


    
#Todoリスト
class Listpage(generic.ListView):
    model = Todo
    template_name = 'todo/listpage.html'

class Createpage(generic.CreateView):
    template_name = 'todo/createpage.html'
    form_class = TodoForm
    success_url = reverse_lazy('spdiary:listpage')  


class Updatepage(generic.UpdateView):
    model = Todo
    template_name = 'todo/updatepage.html'
    fields = ('time','memo')
    success_url = reverse_lazy('spdiary:listpage')  

class Deletepage(generic.DeleteView):
    model = Todo
    template_name = 'todo/deletepage.html'
    success_url = reverse_lazy('spdiary:listpage')            


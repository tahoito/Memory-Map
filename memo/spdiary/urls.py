from django.urls import path
from .views import DiaryApp
from django.contrib.auth import views as auth_views
from .views import SignupPage
from .views import DiaryCreateView
from .views import DiaryCreateCompleteView
from .views import DiaryListView
from .views import DiaryDetailView,DiaryUpdateView,DiaryDeleteView

from .views import Listpage,Createpage,Updatepage,Deletepage

app_name = "spdiary"

urlpatterns = [
    #日記
    path('index/', DiaryApp.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignupPage.as_view(), name='signup'),
    path('create/', DiaryCreateView.as_view(), name='create'),
    path('create/complete/', DiaryCreateCompleteView.as_view(), name='create_complete'),
    path('list/', DiaryListView.as_view(), name='list'),
    path('detail/<uuid:pk>/',DiaryDetailView.as_view(), name = 'detail'), 
    path('update/<uuid:pk>/',DiaryUpdateView.as_view(), name = 'update'), 
    path('delete/<uuid:pk>/',DiaryDeleteView.as_view(),name='delete'),
    #Todoリスト
    path('listpage/',Listpage.as_view(),name='listpage'),
    path('createpage/',Createpage.as_view(),name='createpage'),
    path('updatepage/<int:pk>/',Updatepage.as_view(),name='updatepage'),
    path('deletepage/<int:pk>/',Deletepage.as_view(),name='deletepage'),
]
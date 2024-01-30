from django.urls import path
#from .views import DiaryApp
from django.contrib.auth import views as auth_views
from .views import SignupPage
from .views import DiaryCreateView
from .views import DiaryListView
from .views import DiaryDetailView,DiaryUpdateView,DiaryDeleteView

from .views import ListPage,CreatePage,UpdatePage,DeletePage
from .views import ImageCreateView,ImageListView,ImageDetailView,ImageDeleteView

app_name = "spdiary"

urlpatterns = [
    #register
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignupPage.as_view(), name='signup'),
    #Diary
    path('create/', DiaryCreateView.as_view(), name='create'),
    path('list/', DiaryListView.as_view(), name='list'),
    path('detail/<uuid:pk>/',DiaryDetailView.as_view(), name = 'detail'), 
    path('update/<uuid:pk>/',DiaryUpdateView.as_view(), name = 'update'), 
    path('delete/<uuid:pk>/',DiaryDeleteView.as_view(),name='delete'),
    #imageリスト
    path('Image/',ImageCreateView.as_view(),name='Image'),
    path('ImageList/',ImageListView.as_view(),name='ImageList'),
    path('ImageDetail/<int:pk>/', ImageDetailView.as_view(), name='ImageDetail'),
    path('ImageDelete/<int:pk>/', ImageDeleteView.as_view(), name='ImageDelete'),
    #Todoリスト
    path('ListPage/',ListPage.as_view(),name='ListPage'),
    path('CreatePage/',CreatePage.as_view(),name='CreatePage'),
    path('UpdatePage/<int:pk>/',UpdatePage.as_view(),name='UpdatePage'),
    path('DeletePage/<int:pk>/',DeletePage.as_view(),name='DeletePage'),
]
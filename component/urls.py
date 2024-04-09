from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('login',views.login,name = 'login'),
    path('home',views.home,name = 'home'),
    path('techblog',views.techblog,name = 'techblog'),
    path('hackathon',views.hackathon,name = 'hackathon'),
    path('opportunities',views.opportunities,name = 'opportunities'),
    path('techblog/githubblog/',views.githubblog,name = 'githubblog'),
    path('register',views.register,name = 'register'),
    path('courses',views.courses,name = 'courses'),
    path('linux',views.linux,name = 'linux'),
    path('python',views.python,name = 'python'),
    path('copyright',views.copyright,name = 'copyright'),
    path('contact',views.contact,name = 'contact'),
    path('msg',views.msg,name = 'msg'),
    path("profile_page", views.profile_page, name="profile_page"),
    path("notespedia",views.notespedia,name='notespedia')
]
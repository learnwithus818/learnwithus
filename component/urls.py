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
    path('book',views.book,name = 'book'),
    path('about',views.about,name = 'about'),
    path('msg',views.msg,name = 'msg'),
    path('loginerror',views.loginerror,name = 'loginerror'),
    path('logout',views.logout,name = 'logout'),
    path("profile_page", views.profile_page, name="profile_page"),
    path("cse",views.cse,name='cse'),
    path("et",views.et,name='et'),
    path("notespedia",views.notespedia,name='notespedia'),
    path("team",views.team, name= "team"),
    path("terms_and_conditions",views.terms_and_conditions, name= "terms_and_conditions")

]
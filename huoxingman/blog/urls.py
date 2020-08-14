from django.urls import path,include
from . import views

urlpatterns = [
        path('author/',views.author,name="author"),
        path('category/',views.category,name="category"),
        path('index/',views.index,name="index"),
        path('pageabout/',views.pageabout,name="page-about"),
        path('pagephoto/',views.pagephoto,name="page-photo"),
        path('single/',views.single,name="single"),
        path('singlesidebar/',views.singlesidebar,name="single-sidebar"),
]

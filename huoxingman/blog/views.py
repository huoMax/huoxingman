from django.shortcuts import render

# Create your views here.
def author(request):
    return render(request,'blog/author.html')

def category(request):
    return render(request,'blog/category.html')

def index(request):
    return render(request,'blog/index.html')

def pageabout(request):
    return render(request,'blog/page-about.html')

def pagephoto(request):
    return render(request,'blog/page-photo.html')

def single(request):
    return render(request,'blog/single.html')

def singlesidebar(request):
    return render(request,'blog/single-sidebar.html')


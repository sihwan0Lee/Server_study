from django.shortcuts import render, redirect
from .models import Post

import random
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def blog(request):

    postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist':postlist})

def posting(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article = Post.objects.create(
                postname = request.POST['postname'],
                contents = request.POST['contents'],
                mainphoto = request.POST['mainphoto'],
            )
        else:
            new_article = Post.objects.create(
                postname = request.POST['postname'],
                contents = request.POST['contents'],
                mainphoto = request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')
            
def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})

def lotto(request):
    Lotto_Number_1 = []
    while len(Lotto_Number_1) < 6 :
	    V = random.randint(1,45)
	    if V not in Lotto_Number_1:
		    Lotto_Number_1.append(V)
    print(Lotto_Number_1)
    

    return render(request, 'main/lotto.html', {'Lotto_Number_1':Lotto_Number_1})

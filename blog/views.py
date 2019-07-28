from django.shortcuts import render, get_object_or_404 , redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog, Comment
from .forms import BlogPost, CommentForm
from django.contrib.auth.decorators import login_required

def home(request):
    blogs = Blog.objects #쿼리셋
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page') #request된 page알아내기
    posts = paginator.get_page(page)
    return render(request, 'home.html', { 'blogs' : blogs, 'posts' : posts })


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html' , {'blog' : blog_detail})


#def new(request):
#    return render(request,'new.html')

#def create(request):
#    blog = Blog()
#    blog.title = request.GET['title']
#    blog.body = request.GET['body']
#    blog.pub_date = timezone.datetime.now()
#    blog.save()
#    return redirect('/blog/' + str(blog.id)) #render는 내부에 한정적이라면 , redirect는 외부도 가능하다 . ex)'https://google.com'


def blogpost(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request,'new.html',{'form':form})


@login_required
def comment_new(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method=='POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            return redirect('/blog/' + str(blog.id))
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form})


@login_required
def comment_edit(request, blog_id, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user :
        return redirect('detail', blog_id)

    if request.method=='POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('detail', blog_id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comment_form.html', {'form': form})



@login_required
def comment_delete(request, blog_id, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user :
        return redirect('detail', blog_id)

    if request.method=='POST':
        comment.delete()
        return redirect('detail', blog_id)

    return render(request, 'comment_confirm_delete.html', {'comment':comment})


from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment
from .forms import NewComment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required

# This Function about home 
def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
         posts = paginator.page(paginator.num_pages)    

    context = {
        'title':'الصفحة الرئيسة',
        'posts': posts
    }

    return render(request,'blog/home.html',context)

# This Function about about
def about(request):
    return render(request,'blog/about.html',{'title':'من انا '})

# This Function about post_detail
@login_required(login_url='accounts:login')
def post_detail(request,id):

    post = get_object_or_404(Post,id=id)
    comments = post.comments.filter(active=True)
    comment_form = NewComment()  
    
    # Check before save data  from comment from
    if request.method == 'POST':
         comment_form = NewComment(request.POST)
         if comment_form.is_valid():
             new_comment = comment_form.save(commit=False)
             new_comment.post = post
             new_comment.created_by = request.user
             new_comment.save()
             return redirect('blog:home')
         else:
               comment_form = NewComment()  
    # End of check         

    context = {
        'title':'تفاصيل البوست',
        'post':post,
        'comments':comments,
        'comment_form':comment_form,

    }
    
    return render(request,'blog/post_detail.html',context)

# This Class Based View about PostCreateView
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    template_name = 'blog/new_post.html'
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# This Class Based View about PostUpdateView
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']
    template_name = 'blog/post_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)        

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False        

# This Class Based View about PostDeleteView
class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/blog/home'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author :
            return True
        else:
            return False    

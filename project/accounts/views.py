from django.shortcuts import redirect, render
from .forms import SignUpForm,LoginForm,Profile_update,User_Update
from django.contrib import messages
from django.contrib.auth import authenticate , login as auth_login,logout 
from blog.models import Post
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# This is Function about SignUp
def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            messages.success(request, '.تهانينا {} لقد تمت عملية التسجيل بنجاح'.format(first_name))
            return redirect('accounts:login')
        else:
            form = SignUpForm()
    return render(request,'accounts/signup.html',{'form':form,'title':'التسجيل'})        

# This is Function about Login
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        auth_login(request,user)
        return redirect('accounts:profile')
    else:
          form = LoginForm()  

    return render(request,'accounts/login.html',{'form':form,'title':'تسجيل الدخول'})        

# This is Function about Logout
def logout_user(request):
    logout(request)
    return render(request,'accounts/logout.html',{'title':'تسجيل الخروج'})

# This is Function about Profile
@login_required(login_url='accounts:login')
def profile(request):
    posts = Post.objects.filter(author=request.user)
    post = Post.objects.filter(author=request.user)
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)   
    return render(request,'accounts/profile.html',{'title':'الصفحة الشخصية','posts':posts,'post':post})

# This is Function about Profile_detail
# def profile_detail(request,id):
    profile_detail = Profile.objects.get(id=id)
    posts = Post.objects.filter(author=request.user)
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)  
    return render(request,'accounts/profile_detail.html',{'profile_detail':profile_detail,'title':'الصفحة الشخصية','posts':posts})


# This is Function about Profile_update
@login_required(login_url='accounts:login')
def profile_update(request):    
    user_update = User_Update(instance=request.user)
    profile_update = Profile_update(instance=request.user)
    if request.method == 'POST':
        user_update = User_Update(request.POST,instance=request.user)
        profile_update = Profile_update(request.POST,request.FILES,instance=request.user)
        if user_update.is_valid and profile_update.is_valid:
            user_update.save()
            profile_update.save()
            messages.success( request, 'تم تحديث الملف الشخصي.')
            return redirect('accounts:profile')
        else:    
            user_update = User_Update(instance=request.user)
            profile_update = Profile_update(instance=request.user)

    return render(request,'accounts/profile_update.html',{'title':'تعديل الصفحة الشخصية','user_update':user_update,'profile_update':profile_update})        
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.urls import reverse
from django.template.defaultfilters import slugify

def handler404(request):
    return render(request, '404.html', status=404)

def home(request):
    if request.user.is_authenticated :
        check = profileModel.objects.get(user=request.user)
        if check.writer==True:
            return render(request, 'baseuser.html', )
        if check.regular_user ==True:
            return redirect('list')
    return render(request, 'music/home.html', )

@login_required()
def dashboard(request):
    return render(request, 'music/dashboard.html')

def login_user(request):
    if request.method!= 'POST':
        form = loginForm()
    else:
        form = loginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'Usename or password may have been entered incorrectly.')
                return redirect('login')
    return render(request, 'music/login.html', {'form' : form})

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required()
def profile_user(request, user_name):
    message = ''
    try:
        user = User.objects.get(username = user_name)
        editProfile = False
        #print(request.user.username == user_name)
        if (request.user==user):
            if request.user.is_superuser:
                # contactNumber = None
                editProfile = True
            else:
                # contactNumber  = profileModel.objects.get(user = user).contactNumber
                editProfile = True
        else:
            if request.user.is_superuser:
                # contactNumber  = profileModel.objects.get(user = user).contactNumber
                editProfile = False
            else:
                # contactNumber = None
                editProfile = None
    except:
        user=request.user
        if request.user.is_superuser:
            # contactNumber = None
            editProfile = True
            message = user_name + " Doest Not Exists "
        else:
            # contactNumber  = profileModel.objects.get(user = User.objects.get(username = request.user.username)).contactNumber
            editProfile = True
            message = user_name
    return render(request, 'music/profile.html', { 'editProfile' :editProfile, 'user':user, 'message' : message})
    
def register_user(request):
    if request.method!='POST':
        form = registerForm()
        # form_2 = profileInformForm()
    else:
        form = registerForm(request.POST)
        # form_2 = profileInformForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(form.cleaned_data['password2'])
            user.email = form.cleaned_data['email'].lower()
            user.save()
            profile = profileModel.objects.create(user = user)
            # profile.contactNumber = form_2.cleaned_data['contactNumber']
            profile.save()
            current_site = get_current_site(request)
            message = render_to_string('music/acc_active_email.html', {
                'user':user, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your account.'
            to_email = form.cleaned_data.get('email').lower()
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'music/acc_active_email_confirm.html')
    return render(request, 'music/register.html', {'form' : form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required()
def edit_profile(request):
    if request.method!='POST':
        form = EditProfileForm(instance = request.user)
    else:
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile', args=[request.user.username]))
    return render(request, 'music/edit_profile.html',{'form' : form})

@login_required()
def change_password(request):
    if request.method!='POST':
        form = PasswordChangeForm(user = request.user)
    else:
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(reverse('profile', args=[request.user.username]))
    return render(request, 'music/change_password.html' , {'form': form})

def contact(request):
    if request.method!='POST':
        form = contactForm()
    else:
        form = contactForm(request.POST)
        if form.is_valid():
            mail_subject = 'Contact -- By -- ' + form.cleaned_data.get('userName')
            to_email = settings.EMAIL_HOST_USER
            message = form.cleaned_data.get('body')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('home')
    
    context= {'form' : form}
    return render(request, 'music/contact.html', context)



def BlogList(request):
    Parent = Parent_Category.objects.filter(public=True)
    test = Parent_Category.objects.filter(public=False)
    private_list=[]
    for i in test:
        # print(i.Name , i.Private.all())
        for j in i.Private.all():
            if request.user == j:
                print(j)
                private_list.append(Parent_Category.objects.filter(Name=i.Name))
    print(private_list)
    context = {
    'article':Parent,
    'private':private_list

    }
    return render(request, 'music/list.html', context)

def completeArticle(request, slug):
    parent_cat = Parent_Category.objects.get(slug=slug)
    cat = Category.objects.filter(Parent_Category=parent_cat)

    art={}
    for i in cat:
        articles= Article.objects.filter( catagory=i,status="published")
        art.update({i:articles})
    
    context = {
        'lis':art,
        'Parent':parent_cat,

    }
    return render(request, 'music/complete.html', context)
def BlogDetail(request, slug):
    article = Article.objects.get(slug1=slug,status="published")
    parent_cat = Parent_Category.objects.get(slug=article.slug)
    cat = Category.objects.filter(Parent_Category=parent_cat)

    art={}
    for i in cat:
        articles= Article.objects.filter( catagory=i,status="published")
        art.update({i:articles})


    context = {
        'blogs': article,
        'lis':art

    }
    return render(request, 'music/complete.html', context)

def docview(request):
    form=docform()
    if request.method == 'POST':
        form=docform(request.POST,request.FILES)
        if form.is_valid(): 
            new = form.save(commit=False)
            new.slug=slugify(new.Parent_Category)
            new.slug1=slugify(new.title)
            new.save()
            form.save()
            return redirect('list')
    context={
        'form':form
    }
    return render(request,'music/docs.html',context)


def ParentCategoryview(request):
    form=ParentCategory()
    if request.method == 'POST':
        form=ParentCategory(request.POST,request.FILES)
        if form.is_valid(): 
            new = form.save(commit=False)
            new.slug=slugify(new.Name)
            new.save()
            form.save()
            return redirect('list')
    context={
        'form':form
    }
    return render(request,'music/parent_category.html',context)


def Categoryview(request):
    form=Categoryform()
    if request.method == 'POST':
        form=Categoryform(request)
        if form.is_valid(): 
            new = form.save(commit=False)
            new.slug=slugify(new.Name)
            new.save()
            form.save()
            return redirect('list')
    context={
        'form':form
    }
    return render(request,'music/category.html',context)
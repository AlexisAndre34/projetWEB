from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse 
from app.forms import SignInForm, SignUpFormAccount, GroupForm
from app.models import Account, Category, Publication, Group, File, Comment


#---Homepage views----

def homepage(request):
    account = Account.objects.get(idAccount=request.user.id)
    return render(request, 'homepage.html', locals())
#------login and logout views----------

def login_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"] #hold the validated data
            raw_password = form.cleaned_data["password"]
            user = authenticate(username=username, password=raw_password)
            if user:
                login(request,user)
                return redirect('homepage')
    else:
        form = SignInForm()
    return render(request,'signin.html',locals())

def logout_acc(request):
    logout(request)
    return render(request, 'homepage.html')

#-------creation views---------

def sign_up(request):
    if request.method == 'POST':
        form = SignUpFormAccount(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            acc = User.objects.get(username=username)
            account = Account(idAccount=acc, birthDate=form.cleaned_data.get('birthDate'), department=form.cleaned_data.get('department'), year_in_school=form.cleaned_data.get('year_in_school'), githubLink=form.cleaned_data.get('githubLink'), linkedInLink=form.cleaned_data.get('linkedInLink'),)
            account.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpFormAccount()
    return render(request, 'signin.html', locals())
@login_required
def create_group(request, idAcc):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            account = Account.objects.get(idAccount=idAcc)
            new_group = Group(nameGroup=form.cleaned_data.get('nameGroup'), idAccountGroup_id = idAcc)
            new_group.save()
            base_category = Category(nameCat='general',groupCat=new_group)
            base_category.save()
            return redirect('homepage')#futur redirect on group page 
    else:
        account = Account.objects.get(idAccount=request.user.id)
        form=GroupForm()
    return render(request, 'create/createGroup.html',locals())


    #-------READ VIEWS--------



    #--------UPDATE VIEWS-------

@login_required
def update_account(request):
    user = User.objects.get(id=request.user.id)
    account = Account.objects.get(idAccount=request.user.id)
    if request.method == 'POST':
        form = UpdateAccountForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            account.birthDate = form.cleaned_data.get('birthDate')
            account.department = form.cleaned_data.get('department')
            account.year_in_school = form.cleaned_data.get('year_in_school')
            account.githubLink = form.cleaned_data.get('githubLink')
            account.linkedInLink = form.cleaned_data.get('linkedInLink')
            account.save()
            return redirect('homepage')
    else:
        return render(request, 'update/updateAccount.html', locals())
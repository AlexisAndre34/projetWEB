from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.forms import modelformset_factory
from app.forms import SignInForm, SignUpFormAccount, GroupForm, UpdateAccountForm, PublicationForm, CommentForm, JoinForm
from app.models import Account, Publication, Group, Comment, Join, Belong, File, Admin
from datetime import datetime



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
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            #get the id of user who create the group
            us = User.objects.get(id=request.user.id)
            #create and save the group with the user as groupAdmin
            new_group = Group(nameGroup=form.cleaned_data.get('nameGroup'), idAccountGroup_id=us.id)
            new_group.save()
            #make user the admin of this group
            new_admin = Admin(adminGroup_id=new_group.idGroup, adminAccount_id=us.id)
            new_admin.save()
            #add the user in the member list
            new_belong = Belong(idAccountB_id=us.id, idGroupB_id=new_group.idGroup, joinDate=datetime.now())
            new_belong.save()
            return redirect('homepage')#futur redirect on group page 
    else:
        account = Account.objects.get(idAccount=request.user.id)
        form=GroupForm()
    return render(request, 'create/createGroup.html',locals())



        
        
    



#create a post
@login_required
def create_publication(request, idG):
    FileFormset = modelformset_factory(File, fields=('filef',), extra=3) #will show 4 form of file
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        formset = FileFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            us = User.objects.get(id=request.user.id)
            publication = Publication(titlePubli=form.cleaned_data.get('titlePubli'),contentPubli=form.cleaned_data.get('contentPubli'),datePublished=datetime.now(),idAccountPubli_id=us.id,idGroupPubli_id=idG)
            publication.save()

            for f in formset:
                if f.cleaned_data.get('filef') != None :
                    if formset.is_valid():
                        filef = File(publiFile=publication, filef=f.cleaned_data.get('filef'))
                        filef.save()
                    else:
                        redirect('create_publication', idG)
            return redirect('read_group', idG)
    else:
        form = PublicationForm()
        formset = FileFormset(queryset=File.objects.none())
        context = {
            'form' : form,
            'formset' : formset,
        }
    return render(request, 'create/create_publication.html', context)


    #-------READ VIEWS--------

def read_group(request,idG,idP):
    us = User.objects.get(id=request.user.id)
    group = get_object_or_404(Group,idGroup=idG)
    publicationList = Publication.objects.filter(idGroupPubli=idG).order_by('-datePublished')      #get all the publications of the group
    fileList = []                                                       #contain all the files of all the publication with the id equal to idG
    commentList = []                                                    #contain all the comments of all the publication with the id equal to publication
    for publication in publicationList:
        fileListPubli = File.objects.filter(publiFile=publication)      #list of the files of the publication that are in the group idG
        for fileP in fileListPubli:
            fileList.append(fileP)
        commentListPubli = Comment.objects.filter(idPubliC=publication) #get all the comment of this publication
        for com in commentListPubli:
            name_acc_com = User.objects.get(id=com.idAccountC_id)
            commentList.append(com)                                    #add the comment of publication for each publication
        if idP !=0:
            if request.method == 'POST':
                comment_form = CommentForm(request.POST)
                if comment_form.is_valid():
                    new_comment = Comment(idAccountC_id=us.id, idPubliC_id=idP, comment=comment_form.cleaned_data.get('comment'), commentDate=datetime.now())
                    new_comment.save()
                    return redirect('read_group', idG, 0)
        else:
            comment_form = CommentForm()

    
    return render(request, 'read/group.html', locals())

def read_myaccount(request):
    us = User.objects.get(id=request.user.id)
    account = Account.objects.get(idAccount=request.user.id)
    return render(request, 'read/myaccount.html', locals())

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
            return homepage(request)
    else:
        data={'first_name': user.first_name,'last_name': user.last_name,'email': user.email,'birthDate': account.birthDate,'department': account.department,'year_in_school': account.year_in_school,'githubLink': account.githubLink,'linkedInLink': account.linkedInLink}
        form = UpdateAccountForm(initial=data)
        date = str(account.birthDate.year)+"-"+str(account.birthDate.month)+"-"+str(account.birthDate.day)
    return render(request, 'update/updateAccount.html', locals())


#---------LIST VIEWS--------

#list of group that identified user belong to
@login_required
def group_by_user(request, id):
    #us = User.objects.get(id=request.user.id) not usefull if a get the id through template
    belongList = Belong.objects.filter(idAccountB=id)
    groupList = []
    for group in belongList:
        groupList.append(group.idGroupB)
    
    #count account per group ?
    return render(request,'list/mygroups.html',locals())

def list_groups(request,idG=None):
    us = User.objects.get(id=request.user.id)
    groupsList = Group.objects.all()
    if idG != 0:
        if request.method == 'POST':
            form = JoinForm()
            new_join = Join(idAccountJ_id = us.id, idGroupJ_id=idG)
            new_join.save()
            return redirect('list_groups', 0)
        else:
            join_form = JoinForm()
    return render(request, 'list/listGroups.html', locals())


    
    


    


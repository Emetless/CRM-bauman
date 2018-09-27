import os

from django.contrib import auth
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from CRM import settings
from crmsite.forms import *
from crmsite.models import *


def index(request):
    user = auth.get_user(request)
    if user.is_anonymous:
        return render(request, 'crmsite//index/index.html')
    else:
        return render(request, 'crmsite/index/index.html', {'username': auth.get_user(request)})


def login(request):
    args = {}
    if request.POST:
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден!"
            return render(request, 'crmsite/login.html', args)
    else:
        return render(request, 'crmsite/login.html', args)


def register(request):
    args = {}
    args['form'] = UserSignUpForm
    if request.POST:
        newuser_form = UserSignUpForm(request.POST)
        if request.POST['password'] != request.POST['password_confirmation']:
            return redirect('/register/')
        elif newuser_form.is_valid():
            newRole = Worker.objects.create()
            newRole.save()
            newuser = User.objects.create(username=request.POST['username'],
                                          role_id=newRole.id,
                                          email=request.POST['email'],
                                          first_name=request.POST['first_name'],
                                          last_name=request.POST['last_name'],
                                          caf=request.POST['caf'],
                                          phoneNumber=request.POST['phoneNumber'],
                                          position=request.POST['position'],
                                          commentForAdmin=request.POST['commentForAdmin']
                                          )
            newuser.set_password(request.POST['password_confirmation'])
            newuser.save()
            username = request.POST.get("username", '')
            password = request.POST.get("password", '')
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render(request, 'crmsite/register.html', args)


def profile(request):
    user = auth.get_user(request)
    if user.is_anonymous:
        return render(request, 'crmsite/nonlogin.html')
    else:
        return render(request, 'crmsite/profile.html',
                      {'user': user, 'username': auth.get_user(request), 'username': auth.get_user(request)})


def logout(request):
    auth.logout(request)
    return redirect('/')


def createOrder(request):
    user = auth.get_user(request)
    if user.is_anonymous:
        return render(request, 'crmsite/nonlogin.html')
    elif user.garantAc == True and Worker.objects.get(id=user.role_id).isAuthor == True:
        form = NewOrderForm(request.POST, request.FILES or None)
        if request.POST:
            if form.is_valid():
                if request.POST['isAnalyst'] == 'on':
                    IsAnalyst = True
                if request.POST['isConsult'] == 'on':
                    IsConsult = True
                if request.POST['isTranslator'] == 'on':
                    IsTranslator = True
                if request.POST['isEditor'] == 'on':
                    IsEditor = True
                newOrder = Orders.objects.create(
                    nameJob=request.POST['nameJob'],
                    annotation=request.POST['annotation'],
                    keyWords=request.POST['keyWords'],
                    isAnalyst=IsAnalyst,
                    isConsult=IsConsult,
                    isTranslator=IsTranslator,
                    isEditor=IsEditor,
                    creator=user,
                    Comment=request.POST['Comment'],
                    BlackFile=request.FILES['BlackFile'],
                    Condirion='ПРИНЯТО В РАБОТУ'
                )

                newOrder.save()
                return redirect('/')
            else:
                return render(request, 'crmsite/neworder.html', {'form': form, 'username': auth.get_user(request)})
        else:
            form = NewOrderForm()
            return render(request, 'crmsite/neworder.html', {'form': form, 'username': auth.get_user(request)})
    else:
        return render(request, 'crmsite/nonpermited.html', {'username': auth.get_user(request)})


def orders(request):
    user = auth.get_user(request)
    if user.is_anonymous:
        return render(request, 'crmsite/nonlogin.html')
    elif user.garantAc == True and Worker.objects.get(id=user.role_id).isAuthor == True:
        posts = Orders.objects.filter(creator=user).order_by('createAt')
        return render(request, 'crmsite/orders.html', {'posts': posts, 'username': auth.get_user(request)})
    else:
        return render(request, 'crmsite/nonpermited.html', {'username': auth.get_user(request)})


def orders_detail(request, ids):
    post = get_object_or_404(Orders, id=ids)
    return render(request, 'crmsite/showorder.html', {'post': post})


def adminPanel(request):
    user = auth.get_user(request)
    if user.is_anonymous:
        return render(request, 'crmsite/nonlogin.html')
    elif user.garantAc == True and Worker.objects.get(id=user.role_id).isAdmin == True:
        posts = User.objects.all().order_by('date_joined')
        return render(request, 'crmsite/Administrators/admin.html',
                      {'posts': posts, 'username': auth.get_user(request)})
    else:
        return render(request, 'crmsite/nonpermited.html', {'username': auth.get_user(request)})


def user_detail_admin(request, ids):
    user = auth.get_user(request)
    if user.is_anonymous:
        return render(request, 'crmsite/nonlogin.html')
    elif user.garantAc == True and Worker.objects.get(id=user.role_id).isAdmin == True:
        post = get_object_or_404(User, id=ids)
        form = AdminPanelForm()
        if request.POST:
            IsAdmin, IsAnalyst, IsAuthor, IsChefEditor, IsConsult, IsEditor, IsHead, IsModerator, IsTranslator = False
            if request.POST['isAnalyst'] == 'on':
                IsAnalyst = True
            if request.POST['isConsult'] == 'on':
                IsConsult = True
            if request.POST['isTranslator'] == 'on':
                IsTranslator = True
            if request.POST['isAuthor'] == 'on':
                IsAuthor = True
            if request.POST['isEditor'] == 'on':
                IsEditor = True
            if request.POST['isAdmin'] == 'on':
                IsAdmin = True
            if request.POST['isModerator'] == 'on':
                IsModerator = True
            if request.POST['isChefEditor'] == 'on':
                IsChefEditor = True
            if request.POST['isChefTranslator'] == 'on':
                IsChefTranslator = True
            if request.POST['isHead'] == 'on':
                IsHead = True
            newWorker = Worker.objects.create(isAuthor=IsAuthor,
                                              isEditor=IsEditor,
                                              isTranslator=IsTranslator,
                                              isConsult=IsConsult,
                                              isAnalyst=IsAnalyst,
                                              isAdmin=IsAdmin,
                                              isChefEditor=IsChefEditor,
                                              isChefTranslator=IsChefTranslator,
                                              isModerator=IsModerator,
                                              isHead=IsHead)
            newWorker.save()
            post.role_id = newWorker.id
            if request.POST['garantAC'] == 'on':
                post.garantAc = True
            else:
                post.garantAc = False
            post.save()
            return redirect('admining/')
        else:
            return render(request, 'crmsite/Administrators/useredit.html',
                          {'post': post, 'form': form, 'username': auth.get_user(request)})
    else:
        return render(request, 'crmsite/nonpermited.html', {'username': auth.get_user(request)})


def moderator_panel(request):
    user = auth.get_user(request)
    if user.is_anonymous:
        return render(request, 'crmsite/nonlogin.html')
    elif user.garantAc == True and Worker.objects.get(id=user.role_id).isAdmin == True or Worker.objects.get(
            id=user.role_id).isModerator:
        posts = Orders.objects.exclude(Condirion='ОТКЛОНЕНО').exclude(Condirion='Завершено').order_by('createAt')
        finished = Orders.objects.filter(Condirion=['ОТКЛОНЕНО', 'Завершено']).order_by('Condirion')
        return render(request, 'crmsite/Administrators/moderator.html',
                      {'posts': posts, 'finished': finished, 'username': auth.get_user(request)})
    else:
        return render(request, 'crmsite/nonpermited.html', {'username': auth.get_user(request)})


def moderatorOrderEdit(request, ids):
    user = auth.get_user(request)
    if user.is_anonymous:
        return render(request, 'crmsite/nonlogin.html')
    elif user.garantAc == True and Worker.objects.get(id=user.role_id).isAdmin == True or Worker.objects.get(
            id=user.role_id).isModerator:
        post = Orders.objects.get(id=ids)
        post.moderator = user
        post.save()
        form = ModeratorPanelForm(
            initial={'nameJob': post.nameJob, 'isAnalyst': post.isAnalyst, 'isConsult': post.isConsult,
                     'isTranslator': post.isTranslator, 'isEditor': post.isEditor,
                     'BlackFile': post.BlackFile, 'LastFile': post.LastFile,
                     'Comment': post.Comment, 'annotation': post.annotation, 'keyWords': post.keyWords})
        if request.POST:
            if request.POST['isAnalyst'] == 'on':
                IsAnalyst = True
            if request.POST['isConsult'] == 'on':
                IsConsult = True
            if request.POST['isTranslator'] == 'on':
                IsTranslator = True
            if request.POST['isEditor'] == 'on':
                IsEditor = True
            post.save(nameJob=request.POST['nameJob'],
                      annotation=request.POST['annotation'],
                      keyWords=request.POST['keyWords'],
                      isAnalyst=IsAnalyst,
                      isConsult=IsConsult,
                      isTranslator=IsTranslator,
                      isEditor=IsEditor,
                      creator=user,
                      Comment=request.POST['Comment'],
                      BlackFile=request.FILES['BlackFile'],
                      Condirion=request.POST['Condirion'])

            return redirect('moderating/')
        else:
            return render(request, 'crmsite/Administrators/moderatorOrderEdit.html',
                          {'post': post, 'form': form, 'username': auth.get_user(request)})
    else:
        return render(request, 'crmsite/nonpermited.html', {'username': auth.get_user(request)})


def download(request, ids):
    path = Orders.objects.get(id=ids).BlackFile.path
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="")
            response['Content-Disposition'] = 'inline; filename=' + Orders.objects.get(id=ids).nameJob
            return response
    raise Http404


def show(request):
    print(request.path)
    user = auth.get_user(request)
    if user.is_anonymous:
        return render(request, 'crmsite/nonlogin.html')
    elif user.garantAc == True and Worker.objects.get(id=user.role_id).isTranslator == True:
        posts = Orders.objects.filter(creator=user).order_by('createAt')
        return render(request, 'crmsite/orders.html', {'posts': posts, 'username': auth.get_user(request)})
    else:
        return render(request, 'crmsite/nonpermited.html', {'username': auth.get_user(request)})


def showEdit(request, ids):
    user = auth.get_user(request)
    print(request.path)
    print(ids)
    print(Worker.objects.get(id=user.role_id).isTranslator)

    if user.is_anonymous:
        return render(request, 'crmsite/nonlogin.html')
    elif user.garantAc:
        if Worker.objects.get(id=user.role_id).isTranslator:
            post = get_object_or_404(Orders, id=ids, isTranslator=True)
            CondirionS = 'ПЕРЕДАНО ПЕРЕВОДЧИКУ'
            print(post)
        elif Worker.objects.get(id=user.role_id).isEditor and request.path == '/editor/' + str(ids):
            post = get_object_or_404(Orders, id=ids, isEditor=True)
            CondirionS = 'ПЕРЕДАНО РЕДАКТОРУ'
        elif Worker.objects.get(id=user.role_id).isConsult and request.path == '/consultant/' + str(ids):
            post = get_object_or_404(Orders, id=ids, isConsult=True)
            CondirionS = 'ПЕРЕДАНО КОНСУЛЬТАНТАМ'
        elif Worker.objects.get(id=user.role_id).isAnalyst and request.path == '/analyst/' + str(ids):
            post = get_object_or_404(Orders, id=ids, isAnalyst=True)
            CondirionS = 'ПЕРЕДАНО ПЕРЕВОДЧИКУ'
        else:
            return redirect('/')
        form = EditWorkerForm(request.POST, request.FILES or None)
        if request.POST:
            post.save(aciveBy=request.POST['aciveBy'],
                      Comment=request.POST['Comment'],
                      LastFile=request.FILES['LastFile'],
                      Condirion=CondirionS)
            return redirect(request.path)
        return render(request, 'crmsite/showorder.html', {'post': post, 'form': form})
    else:
        return render(request, 'crmsite/nonpermited.html', {'username': auth.get_user(request)})

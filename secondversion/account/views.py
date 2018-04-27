from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

def signup(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        if form1.is_valid():
            form1.save()
            username = form1.cleaned_data.get('username')
            raw_password = form1.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index.html')
    else:
        form1 = UserCreationForm()
    return render(request, 'signup.html', {'form1': form1})



def signupandlogin(request):
    if request.method == "POST":
        if request.POST.get('submit') == "signupbutton":
            if request.method == 'POST':
                form1 = UserCreationForm(request.POST)
                if form1.is_valid():
                    form1.save()
                    username = form1.cleaned_data.get('username')
                    raw_password = form1.cleaned_data.get('password1')
                    user = authenticate(username=username, password=raw_password)
                    login(request, user)
                    return redirect('home')
            else:
                form1 = UserCreationForm()
            return render(request, 'signup.html', {'form1': form1})
        elif request.POST.get('submit') == "loginbutton":
            if request.method == 'POST':
                form2 = AuthenticationForm(data=request.POST)
                if form2.is_valid():
                    cd = form2.cleaned_data
                    user = authenticate(username=cd['username'], password=cd['password'])
                    if user is not None:
                        if user.is_active:
                            login(request, user)
                            return HttpResponse('Authenticated successfully')
                        else:
                            return HttpResponse('Disabled account')
                    else:
                        return HttpResponse('Invalid login')
            else:
                form2 = AuthenticationForm()
            return render(request, 'login.html', {'form2': form2})
        else:
            return HttpResponse("What button did you click?")
    else:
        form1 = UserCreationForm(request.POST)
        form2 = AuthenticationForm(data=request.POST)
        return render(request, 'testcombine.html', {'form1': form1,'form2':form2})


def login_user(request):
    if request.method == 'POST':
        form2 = AuthenticationForm(data=request.POST)
        if form2.is_valid():
            cd = form2.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form2 = AuthenticationForm()
    return render(request, 'login.html', {'form2': form2})



def index(request):
    return render(request, 'index.html')



    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(username=username, password=raw_password)
    # if user is not None:
    #     if user.is_active:
    #         login(request,user)
    #         return redirect('home')
    #     else:
    #         return HttpResponse('Disabled account')
    # else:
    #     return HttpResponse('Invalid login')


# #authentication form
# def userlogin(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})

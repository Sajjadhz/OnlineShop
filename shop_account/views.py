from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm, ResisterForm, EditUserForm
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib.auth.models import User
from django.http import Http404


# Create your views here.

def login_user(request):
    # Note that we need to declare form method as post within related html file
    # these two following lines prevent the login page to be shown for users who already logged into the site
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():  # here we validate the input user's data
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        # print(user) # here user is simply user's name
        # print(login_form.cleaned_data)  # Cleaned_data is a dictionary including username and password
        if user is not None:  # here we check user's existence in database
            login(request, user)
            # print("Success")
            return redirect('/')
        else:
            print("Error")
            # this line informs user about errors in input data
            login_form.add_error('user_name', 'کاربری با مشخصات وارد شده یافت نشد')

    context = {
        'login_form': login_form
    }
    # here we do not need to include app name to address html templates files
    return render(request, 'account/login.html', context)


def register(request):
    # these two following lines prevent the register page to be shown for users who already logged into the site
    if request.user.is_authenticated:
        return redirect('/')
    register_form = ResisterForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')

        User.objects.create_user(username=user_name, email=email, password=password)
        return redirect('/login')
    context = {
        'register_form': register_form
    }
    # here we do not need to include app name to address html templates files
    return render(request, 'account/register.html', context)


def log_out(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def user_account_main_page(request):
    return render(request, 'account/user_account_main.html', {})


@login_required(login_url='/login')
def edit_user_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')

    edit_user_form = EditUserForm(request.POST or None,
                                  initial={'first_name': user.first_name, 'last_name': user.last_name})
    print(user.first_name)
    print(user.last_name)

    if edit_user_form.is_valid():
        first_name = edit_user_form.cleaned_data.get('first_name')
        last_name = edit_user_form.cleaned_data.get('last_name')

        user.first_name = first_name
        user.last_name = last_name
        user.save()
    context = {'edit_form': edit_user_form}
    return render(request, 'account/edit_account.html', context)


def user_sidebar(request):
    return render(request, 'account/user_sidebar.html', {})

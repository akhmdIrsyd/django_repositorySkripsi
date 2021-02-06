from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, HttpResponse

from .models import mahasiswa,dosen,User
# Create your views here.

from django.urls import reverse_lazy

#forms
from .forms import MHSModelForm, DosenModelForm, CustomUserCreationForm, LoginForm, SignupForm, MHSdetailForm, skripsidetailForm
#modal
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
#decorators
from .decorators import mahasiswa_required, admin_required, dosen_required

from django.views import generic

from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.hashers import make_password
from django.contrib import messages

class MHSUpdateView(BSModalUpdateView):
    model = mahasiswa
    template_name = 'web/form.html'
    form_class = MHSModelForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('mahasiswa')


class MHSDeleteView(BSModalDeleteView):
    model = mahasiswa
    template_name = 'web/form_delete.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('mahasiswa')


class MHSCreateView(BSModalCreateView):
    template_name = 'web/form.html'
    form_class = MHSModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('mahasiswa')


class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'web/form.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('akun')


class akunUpdateView(BSModalUpdateView):
    model = User
    template_name = 'web/form.html'
    form_class = CustomUserCreationForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('akun')


class akunDeleteView(BSModalDeleteView):
    model = User
    template_name = 'web/form_delete.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('akun')


class DosenUpdateView(BSModalUpdateView):
    model = dosen
    template_name = 'web/form.html'
    form_class = DosenModelForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('dosen')


class DosenDeleteView(BSModalDeleteView):
    model = dosen
    template_name = 'web/form_delete.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('dosen')


class DosenCreateView(generic.CreateView):
    template_name = 'web/form.html'
    form_class = DosenModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('dosen')


@csrf_protect
def Login(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')  # Get email value from form
        password = request.POST.get('password')  # Get password value from form
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #type_obj = user_type.objects.get(user=user)
            #if user.is_authenticated and type_obj.is_student:
            if user.is_authenticated:
                return redirect('index')  # Go to student home
            #elif user.is_authenticated and type_obj.is_teach:
            #elif user.is_authenticated and user.user_type == 2:
             #   return redirect('Pendaftar')  # Go to teacher home
        else:
            # Invalid email or password. Handle as you wish
            return redirect('login')

    return render(request, 'web/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'web/signup.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    #Data_siswa = data_siswa.objects.all()
    context = {
    }
    return render(request, 'web/index.html', context)


@login_required
@admin_required
def list_akun(request):
    Data_akun = User.objects.all()
    context = {
        'rows': Data_akun,
    }
    return render(request, 'web/akun.html', context)


@login_required
@admin_required
def list_mahasiswa(request):
    Data_mhs = mahasiswa.objects.all()
    context = {
        'rows': Data_mhs,
    }
    return render(request, 'web/mahasiswa.html', context)


@login_required
@admin_required
def list_dosen(request):
    Data_dosen = dosen.objects.all()
    context = {
        'rows': Data_dosen,
    }
    return render(request, 'web/dosen.html', context)


@login_required
@mahasiswa_required
def detail_skripsi(request):
    user=request.user
    data_skripsi = mahasiswa.objects.get(nim=user.id)
    if request.method == 'POST':
        form = skripsidetailForm(request.POST, request.FILES, instance=data_skripsi)
        
        if form.is_valid():
            form.save()
            return redirect('skripsi')
    else:
        
        form = skripsidetailForm(instance=data_skripsi)
    context = {
        'form': form,
    }
    return render(request, 'web/detail_skripsi.html', context)


@login_required
@mahasiswa_required
def detail_dataMHS(request):
    user = request.user
    data_skripsi = mahasiswa.objects.get(nim=user.id)
    if request.method == 'POST':
        form = MHSdetailForm(request.POST, request.FILES, instance=data_skripsi)

        if form.is_valid():
            form.save()
            return redirect('data_mahasiswa')
    else:

        form = MHSdetailForm(instance=data_skripsi)
    context = {
        'form': form,
    }
    return render(request, 'web/detail_skripsi.html', context)


@login_required
@dosen_required
def detail_dataDosen(request):
    user = request.user
    data_dosen = dosen.objects.get(username=user.id)
    if request.method == 'POST':
        form = DosenModelForm(request.POST, request.FILES, instance=data_dosen)

        if form.is_valid():
            form.save()
            return redirect('data_dosen')
    else:
        form = DosenModelForm(instance=data_dosen)
    context = {
        'form': form,
    }
    return render(request, 'web/detail_skripsi.html', context)


@login_required
@dosen_required
def list_skripsiDosen(request):
    user = request.user
    print(user.id)
    dosendetail = dosen.objects.get(username=user.id)
    Data_skripsi = mahasiswa.objects.filter(pembimbing1=dosendetail.id) |  mahasiswa.objects.filter(pembimbing2=dosendetail.id)
    
    context = {
        'rows': Data_skripsi,
    }
    return render(request, 'web/mahasiswa.html', context)

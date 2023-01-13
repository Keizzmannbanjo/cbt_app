
from django.shortcuts import render, redirect, reverse

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import logging


from .forms import SignInForm
from student.forms import StudentCreationForm
from lecturer.forms import LecturerCreationForm, SubjectCreationForm

logger = logging.getLogger('django')


def generalSignIn(request):
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                if user.type == 'student':
                    login(request, user)
                    return redirect(reverse('student:dashboard'))
                elif user.type == 'lecturer':
                    login(request, user)
                    return redirect(reverse('lecturer:dashboard'))
            else:
                return render(request, 'accounts/signin.html', {'form': form, 'invalidUser': True})

    return render(request, 'accounts/signin.html', {'form': form, 'invalidUser': False})


def registrarSignIn(request):
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get(
                'username'), password=form.cleaned_data.get('password'))
            if user:
                login(request, user)
                return redirect(reverse('accounts:registrar_dashboard'))
    return render(request, 'registrar/signin.html', {'form': form})


@login_required
def createStudent(request):
    form = StudentCreationForm()
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:registrar_dashboard'))
    return render(request, 'registrar/create.html', {'form': form})


@login_required
def createLecturer(request):
    form = LecturerCreationForm()
    if request.method == 'POST':
        form = LecturerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:registrar_dashboard'))
    return render(request, 'registrar/create.html', {'form': form})


@login_required
def createSubject(request):
    form = SubjectCreationForm()
    if request.method == 'POST':
        form = SubjectCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:registrar_dashboard'))

    return render(request, 'registrar/create_subject.html', {'form': form})


@login_required
def registrarDashboard(request):
    return render(request, 'registrar/dashboard.html')

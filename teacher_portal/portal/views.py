from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


@login_required
def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        subject = request.POST.get('subject').strip()
        marks = request.POST.get('marks').strip()

        if not (name and subject and marks):
            messages.error(request, 'All fields are required.')
            return redirect('home')

        marks = int(marks)

        student, created = Student.objects.get_or_create(name=name, subject=subject)
        if created:
            student.marks = marks
            messages.success(request, 'New student added successfully!')
        else:
            student.marks = marks
            messages.success(request, 'Existing student found — marks updated!')

        student.save()
        return redirect('home')

@login_required
def edit_student(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(id=student_id)
        student.name = request.POST['name']
        student.subject = request.POST['subject']
        student.marks = request.POST['marks']
        student.save()
    return redirect('home')


@login_required
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('home')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created. Please log in.')
            return redirect('login')

    return render(request, 'signup.html')

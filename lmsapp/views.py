from django.shortcuts import render, redirect
from .models import student
from .models import teacher
from django.contrib import messages
from django.contrib.auth import authenticate,login as log, logout


def home(request):
    return render(request, "index.html")

def studentlogin(request):
    return render(request, 'studentlogin.html')

# def user_studentlogin(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     student_obj = student.objects.filter(username=username, password=password).first()
    #     if student_obj:
    #         # Store student id in session
    #         request.session['student_id'] = student_obj.id
    #         return redirect('studentdashboard')
    #     else:
    #         messages.error(request, 'Invalid username or password')
    #         return render(request, 'studentlogin.html')
    # return render(request, 'studentlogin.html')
def user_studentlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        cr = student.objects.filter(username=username, password=password)
        if cr.exists():
            user_details = student.objects.get(username=username, password=password)
            request.session['id'] = user_details.id
            request.session['name'] = user_details.name
            


            return redirect('studentdashboard')
        else:
            return render(request, 'studentlogin.html', {'error': 'Invalid Email or Password'})
    
    return render(request, 'studentlogin.html')

def studentdashboard(request):
    id = request.session.get('id')
    name = request.session.get('name')
    return render(request,'studentdashboard.html',{'id':id,'name':name})


def studentregister(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        department = request.POST.get('department')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        password = request.POST.get('password')
        student(name=name, year=year, department=department, email=email,
                phone=phone, username=username, password=password).save()
        messages.success(request, "Registration successful!")
    return render(request, "studentregister.html")


def student_edit(request):
    student_id = request.session.get('id')
    if not student_id:
        messages.error(request, "You must login first")
        return redirect('studentlogin')

    stud = student.objects.get(id=student_id)
    if request.method == 'POST':
        stud.name = request.POST.get('name')
        stud.email = request.POST.get('email')
        stud.year = request.POST.get('year')
        stud.phone = request.POST.get('phone')
        stud.username = request.POST.get('username')
        stud.password = request.POST.get('password')
        stud.department = request.POST.get('department')
        stud.save()
        messages.success(request, "Profile updated successfully!")
    return render(request, 'student_edit.html', {'student': stud})

def studentlogout(request):
    logout(request)
    return redirect('studentlogin')


def student_profile(request):
    student_id = request.session.get('id')
    cr = student.objects.get(id=student_id)   # or student_id=student_id, depending on your model field name
    return render(request, 'student_profile.html', {'cr': cr})

def apply_leave(request):
    return render(request,"apply_leave.html")

def teacherlogin(request):
    return render(request, 'teacherlogin.html')

def teacherregister(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        department = request.POST.get('department')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        password = request.POST.get('password')
        teacher(name=name, subject=subject, department=department, email=email,
                phone=phone, username=username, password=password).save()
        messages.success(request, "Registration successful!")
    return render(request, "teacherregister.html")


def user_teacherlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        cr = teacher.objects.filter(username=username, password=password)
        if cr.exists():
            user_details = teacher.objects.get(username=username, password=password)
            request.session['id'] = user_details.id
            request.session['name'] = user_details.name
            


            return redirect('teacherdashboard')
        else:
            return render(request, 'teacherlogin.html', {'error': 'Invalid Email or Password'})
    
    return render(request, 'teacherlogin.html')

def teacherdashboard(request):
    id = request.session.get('id')
    name = request.session.get('name')
    return render(request,'teacherdashboard.html',{'id':id,'name':name})
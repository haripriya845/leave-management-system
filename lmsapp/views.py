from django.shortcuts import render, redirect,get_object_or_404
from .models import student
from .models import teacher,leave
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
    student_id = request.session.get('id')
    if not student_id:
        messages.error(request, "You must login first")
        return redirect('studentlogin')

    cr = student.objects.get(id=student_id)

    if request.method == 'POST':
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        leave.objects.create(student=cr, subject=subject, content=content)
        messages.success(request, "Leave request submitted successfully!")
        return redirect('studentdashboard')

    return render(request, "apply_leave.html", {'cr': cr})


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


def teacherlogout(request):
    logout(request)
    return redirect('teacherlogin')


def teacher_profile(request):
    teacher_id = request.session.get('id')
    cr = teacher.objects.get(id=teacher_id)   # or student_id=student_id, depending on your model field name
    return render(request, 'teacher_profile.html', {'cr': cr})

def teacher_edit(request):
    teacher_id = request.session.get('id')
    if not teacher_id:
        messages.error(request, "You must login first")
        return redirect('teacherlogin')

    teach = teacher.objects.get(id=teacher_id)
    if request.method == 'POST':
        teach.name = request.POST.get('name')
        teach.email = request.POST.get('email')
        teach.subject = request.POST.get('subject')
        teach.phone = request.POST.get('phone')
        teach.username = request.POST.get('username')
        teach.password = request.POST.get('password')
        teach.department = request.POST.get('department')
        teach.save()
        messages.success(request, "Profile updated successfully!")
    return render(request, 'teacher_edit.html', {'teach': teach})


def leave_details(request):
    teacher_id = request.session.get('id')

    if not teacher_id:
        return redirect('teacherlogin')

    teacher_obj = teacher.objects.get(id=teacher_id)

    leaves = leave.objects.filter(student__department=teacher_obj.department,status='Pending').order_by('-date_applied', '-time_applied')

    return render(request, 'leave_details.html', {'leaves': leaves, 'department': teacher_obj.department})


def student_details(request):
    teacher_id = request.session.get('id')

    if not teacher_id:
        return redirect('teacherlogin')

    teacher_obj = teacher.objects.get(id=teacher_id)

    students = student.objects.filter(department=teacher_obj.department).order_by('name')

    return render(request, 'student_details.html', {
        'students': students,
        'department': teacher_obj.department
    })

def approved_leave(request):
    teacher_id = request.session.get('id')
    if not teacher_id:
        return redirect('teacherlogin')

    teacher_obj = teacher.objects.get(id=teacher_id)
    approved_leaves = leave.objects.filter(student__department=teacher_obj.department, status='Approved')

    return render(request, 'approved_leave.html', {
        'leaves': approved_leaves,
        'department': teacher_obj.department
    })

def approve_leave(request, id):
    leave_obj = get_object_or_404(leave, id=id)
    leave_obj.status = 'Approved'
    leave_obj.save()
    return redirect('leave_details')


def delete_leave(request, id):
    leave_obj = get_object_or_404(leave, id=id)
    leave_obj.delete()
    return redirect('leave_details')
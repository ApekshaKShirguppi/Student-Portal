from django.shortcuts  import render,redirect
from student.models import Stuednt_feedback,Student_Notification,Branch,Student_list,CustomUser,Staff,Subject,Staff_Notification
from django.contrib import messages


def HOME(request):
    student_count = Student_list.objects.all().count()
    staff_count = Staff.objects.all().count()
    branch_count = Branch.objects.all().count()
    subject_count = Subject.objects.all().count()

    context = {
        'student_count':student_count,
        'staff_count': staff_count,
        'subject_count':subject_count,
        'branch_count':branch_count,
    }
    return render(request,'Hod/home.html',context)


def ADD_STUDENT(request):
    branch = Branch.objects.all()

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        branch_id = request.POST.get('branch_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Enter different email as it is already taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Enter different UserName as it is already taken')
            return redirect('add_student')
        else:

            user = CustomUser(
               first_name=first_name,
               last_name=last_name,
               username=username,
               email=email,
               user_type=3
            )
            user.set_password(password)
            user.save()

        branch = Branch.objects.get(id=branch_id)

        student_list = Student_list(
            admin=user,

            address=address,
            branch_id=branch,
            gender=gender,
        )
        student_list.save()
        messages.success(request, user.first_name+" "+user.last_name + "student is saved")
        return redirect('add_student')

    context = {
        'branch': branch,
    }
    return render(request,'Hod/add_student.html',context)


def VIEW_STUDENT(request):
    students = Student_list.objects.all()
    context = {
        'students':students,
    }
    return render(request,'Hod/view_student.html',context)


def EDIT_STUDENT(request,id):
    studente = Student_list.objects.filter(id=id)
    branch = Branch.objects.all()

    context ={
        'studente':studente,
        'branch':branch
    }
    return render(request,'Hod/edit_student.html',context)


def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id=request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        branch_id = request.POST.get('branch_id')

        user = CustomUser.objects.get(id=student_id)

        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.username=username

        if password!=None and password !="":
            user.set_Password(password)
        user.save()

        student = Student_list.objects.get(admin=student_id)
        student.address=address
        student.gender=gender

        branch=Branch.objects.get(id = branch_id)
        student.branch_id=branch

        student.save()
        messages.success(request,'Record is Updated')
        return redirect('view_student')

    return render(request,'Hod/edit_student.html')


def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,'Record deleted!')
    return redirect('view_student')


def ADD_BRANCH(request):
    if request.method == "POST":
        branch_name = request.POST.get('branch_name')

        branch = Branch(
            name = branch_name,
        )

        branch.save()
        messages.success(request,'Branch Added')
        return redirect('add_branch')

    return render(request,'Hod/add_branch.html')


def VIEW_BRANCH(request):
    branch = Branch.objects.all()
    context = {
        'branch': branch
    }

    return render(request,'Hod/view_branch.html',context)


def EDIT_BRANCH(request,id):
    branch = Branch.objects.get(id = id)
    context = {
        'branch': branch
    }
    return render(request,'Hod/edit_branch.html',context)


def UPDATE_BRANCH(request):
    if request.method == "POST":
        name = request.POST.get('name')
        branch_id = request.POST.get('branch_id')

        branch =Branch.objects.get(id = branch_id)
        branch.name = name
        branch.save()
        messages.success(request,'Record Updated')
        return redirect('view_branch')
    return render(request,'Hod/edit_branch.html')


def DELETE_BRANCH(request,id):
    branch=Branch.objects.get(id=id)
    branch.delete()
    messages.success(request,'Branch Deleted')
    return redirect('view_branch')


def ADD_STAFF(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email id is already taken')
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Enter different user name')
            return redirect('add_staff')
        else:
            user = CustomUser(first_name=first_name,last_name=last_name,email=email,user_type=2,username=username)
            user.set_password(password)
            user.save()

            staff = Staff(
                admin = user,
                address = address,
                gender = gender,
            )
            staff.save()
            messages.success(request,'Record saved')
            return redirect('add_staff')
    return render(request,'Hod/add_staff.html')


def VIEW_STAFF(request):

    staff=Staff.objects.all()
    context = {
        'staff':staff
    }
    return render(request,'Hod/view_staff.html',context)


def EDIT_STAFF(request,id):
    staff = Staff.objects.get(id=id)

    context ={
        'staff':staff
    }
    return render(request,'Hod/edit_staff.html',context )


def UPDATE_STAFF(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password!=None and password !="":
            user.set_Password(password)

        user.save()

        staff = Staff.objects.get(admin = staff_id)
        staff.gender = gender
        staff.address = address

        staff.save()

        messages.success(request,'Changes saved')
        return redirect('view_staff')

    return render(request, 'Hod/edit_staff.html')


def DELETE_STAFF(request,admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request,'Record deleted')
    return redirect('view_staff')


def ADD_SUBJECT(request):
    branch = Branch.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        branch_id = request.POST.get('branch_id')
        staff_id = request.POST.get('staff_id')

        branch = Branch.objects.get(id=branch_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            name =name,
            branch = branch,
            staff=staff,
        )

        subject.save()
        messages.success(request,'Record saved')
        return redirect('add_subject')
    context = {
         'branch': branch,
         'staff': staff,
    }
    return render(request,'Hod/add_subject.html',context)


def VIEW_SUBJECT(request):
    subject = Subject.objects.all()
    context = {
        'subject':subject
    }

    return render(request,'Hod/view_subject.html',context)


def EDIT_SUBJECT(request,id):
    subject = Subject.objects.get(id = id)
    branch = Branch.objects.all()
    staff = Staff.objects.all()

    context = {
        'subject':subject,
        'branch':branch,
        'staff':staff,
    }
    return render(request,'Hod/edit_subject.html',context)


def UPDATE_SUBJECT(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject_id = request.POST.get('subject_id')
        branch_id = request.POST.get('branch_id')
        staff_id = request.POST.get('staff_id')

        branch = Branch.objects.get(id = branch_id)
        staff = Staff.objects.get(id = staff_id)

        subject = Subject(
            id = subject_id,
            name = name,
            branch = branch,
            staff = staff

        )
        subject.save()
        messages.success(request,'Record updated')
        return redirect('view_subject')


def DELETE_SUBJECT(request,id):
    subject = Subject.objects.filter(id = id)
    subject.delete()
    messages.success(request,'Record Deleted')
    return redirect('view_subject')


def STAFF_SEND_NOTIFICATION(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')[0:5]

    context = {
         'staff' : staff,
         'see_notification' : see_notification,

    }
    return render(request,'Hod/staff_notification.html',context)


def SAVE_STAFF_NOTIFICATION(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')
        staff = Staff.objects.get(admin = staff_id)
        notification = Staff_Notification(
            staff_id = staff,
            message = message,
        )
        notification.save()
        messages.success(request,'Notification is sent')
        return redirect('staff_send_notification')

    return None


def STUD_NOTIFICATIONS(request):
    student_list= Student_list.objects.all()
    notification = Staff_Notification.objects.all()
    context = {
        'notification':notification,
        'student_list':student_list,
    }
    return render(request,'Hod/student_noti.html',context)


def SAVE_STUD_NOTI(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        message = request.POST.get('message')
        student_list = Student_list.objects.get(admin=student_id)

        student_notifi = Student_Notification(
            student_id = student_list,
            message = message,
        )
        student_notifi.save()
        messages.success(request, 'Notification is sent')
    return redirect('stud_notifications')


def STUDENT_FEEDBACK(request):
    feedback = Stuednt_feedback.objects.all()
    feedback_history = Stuednt_feedback.objects.all()

    context = {
        'feedback':feedback,
        'feedback_history':feedback_history,
    }
    return render(request,'Hod/student_feedback.html',context)


def F_REPLY(request):
    if request.method=="POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')
        feedback = Stuednt_feedback.objects.get(id = feedback_id)

        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        return redirect('student_feedback')



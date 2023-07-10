from django.shortcuts import render,redirect
from student.models import StudentResult,Subject,Staff,Staff_Notification,Student_list
from django.contrib import messages

def HOME(request):
    return render(request,'Staff/home.html')


def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id

        notification = Staff_Notification.objects.filter(staff_id = staff_id)

        context = {
             'notification':notification
        }
        return render(request,'Staff/notifications.html',context)


def MARK_NOTIFICATION(request,status):
    notification = Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notifications')


def STAFF_TAKE_ATTEND(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    subject = Subject.objects.filter(staff = staff_id)
    action = request.GET.get('action')

    students = None
    get_subject = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')

            get_subject = Subject.objects.filter(id = subject_id)

            subject = Subject.objects.filter(id = subject_id)
            for i in subject:
                student_id = i.branch.id
                students = Student_list.objects.filter(branch_id = student_id)

    context = {
        'subject':subject,
        'get_subject':get_subject,
        'action':action,
        'students':students
    }
    return render(request,'Staff/take_attendance.html',context)


def STAFF_SAVE_ATTENDANCE(request):

    return None


def STAFF_ADD_RESULT(request):
    staff = Staff.objects.get(admin = request.user.id)

    subjects = Subject.objects.filter(staff_id = staff)
    action = request.GET.get('action')

    get_subject=None
    students= None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')

            get_subject = Subject.objects.get(id = subject_id)
            subjects1 = Subject.objects.all().get(id = subject_id)
            for i in subjects:
                student_id = i.branch.id
                students = Student_list.objects.filter(branch_id = student_id)


    context={
        'subjects': subjects,
        'action':action,
        'get_subject':get_subject,
        'students':students,
    }
    return render(request,'Staff/add_result.html',context)


def STAFF_SAVE_RES(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        student_id = request.POST.get('student_id')
        cie_marks = request.POST.get('cie_marks')
        exam_marks = request.POST.get('exam_marks')
        get_student = Student_list.objects.get(admin = student_id)
        get_subject = Subject.objects.get(id = subject_id)

        check_exists = StudentResult.objects.filter(subject_id = get_subject,student_id=get_student).exists()
        if check_exists:
            result = StudentResult.objects.get(subject_id = get_subject, student_id = get_student)
            result.cta_marks = cie_marks
            result.marks_in_end_sem = exam_marks
            result.save()
            messages.success(request,'Result updated')
            return redirect('staff_save_res')
        else:
            result = StudentResult(
                student_id = get_student,
                subject_id = get_subject,
                marks_in_end_sem = exam_marks,
                cta_marks = cie_marks,

            )
            result.save()
            messages.success(request, 'Result added')
            return redirect('staff_save_res')

    return redirect('staff_add_result')



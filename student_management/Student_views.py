from django.shortcuts import render,redirect
from student.models import StudentResult,Stuednt_feedback,Student_list,Student_Notification

def HOME(request):
    return render(request,'Student/home.html')


def S_NOTIFICATIONS(request):
    student = Student_list.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id

        notification = Student_Notification.objects.filter(student_id = student_id)

        context = {
            'notification': notification
        }
    return render(request,'Student/noti.html',context)


def MARK_NOTI(request,status):
    notification = Student_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('s_notifications')


def STUDENT_FEED(request):
    student_id = Student_list.objects.get(admin=request.user.id)
    feedback_history=Stuednt_feedback.objects.filter(student_id=student_id)

    context = {
        'feedback_history':feedback_history,
    }
    return render(request,'Student/feedback.html',context)


def SAVE_FEEDBACK(request):

    if request.method =="POST":
        feedback = request.POST.get('feedback')
        student_ = Student_list.objects.get(admin = request.user.id)
        feedback = Stuednt_feedback(
            student_id=student_,
            feedback=feedback,
            feedback_reply='',
        )
        feedback.save()
        return redirect('student_feed')

def VIEW_RESULT(request):
    student = Student_list.objects.get(admin = request.user.id)
    res = StudentResult.objects.filter(student_id = student)
    context = {
        'res': res,
    }
    return render(request,'student/view_result.html',context)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import StudentProfile, Marks


@login_required(login_url='/login/')
def dashboard_view(request):
    try:
        profile = StudentProfile.objects.get(user=request.user)
        marks = Marks.objects.filter(student=profile)
        total_subjects = marks.count()
        marks_list = list(marks)
        passed_subjects = sum(1 for m in marks_list if m.grade != 'U')
        failed_subjects = sum(1 for m in marks_list if m.grade == 'U')
        if marks_list:
            total_credits = sum(m.subject.credits for m in marks_list)
            total_points = sum(m.subject.credits * m.grade_point for m in marks_list)
            cgpa = round(total_points / total_credits, 2) if total_credits > 0 else 0
        else:
            cgpa = 0
        return render(request, 'dashboard.html', {
            'profile': profile,
            'cgpa': cgpa,
            'total_subjects': total_subjects,
            'passed_subjects': passed_subjects,
            'failed_subjects': failed_subjects,
        })
    except StudentProfile.DoesNotExist:
        return redirect('/login/')


@login_required(login_url='/login/')
def marks_view(request):
    try:
        profile = StudentProfile.objects.get(user=request.user)
        marks = Marks.objects.filter(student=profile)
        marks_list = list(marks)
        if marks_list:
            total_credits = sum(m.subject.credits for m in marks_list)
            total_points = sum(m.subject.credits * m.grade_point for m in marks_list)
            cgpa = round(total_points / total_credits, 2) if total_credits > 0 else 0
        else:
            cgpa = 0
        total_marks = sum(m.total_marks for m in marks_list)
        pass_status = 'Fail' if any(m.grade == 'U' for m in marks_list) else 'Pass'
        return render(request, 'results/list.html', {
            'profile': profile,
            'marks': marks_list,
            'cgpa': cgpa,
            'total_marks': total_marks,
            'pass_status': pass_status,
        })
    except StudentProfile.DoesNotExist:
        return redirect('/login/')


@login_required(login_url='/login/')
def cgpa_view(request):
    try:
        profile = StudentProfile.objects.get(user=request.user)
        marks = Marks.objects.filter(student=profile)
        marks_list = list(marks)
        if marks_list:
            total_credits = sum(m.subject.credits for m in marks_list)
            total_points = sum(m.subject.credits * m.grade_point for m in marks_list)
            cgpa = round(total_points / total_credits, 2) if total_credits > 0 else 0
        else:
            cgpa = 0
        return render(request, 'results/cgpa.html', {
            'profile': profile,
            'marks': marks_list,
            'cgpa': cgpa,
        })
    except StudentProfile.DoesNotExist:
        return redirect('/login/')


@login_required(login_url='/login/')
def components_view(request):
    return render(request, 'components.html')
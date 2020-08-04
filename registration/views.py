from django.shortcuts import render
from registration.models import *
# Create your views here.
def index(request,class_id,sub_id):
    rec_class=Classroom.objects.get(c_id=class_id)
    sub=Subjects.objects.get(sub_id=sub_id)
    print(sub)
    student_list2=Student.objects.filter(s_class=rec_class)
    context={
        "class":rec_class,
        "subject":sub,
        "students":student_list2
    }
    return render(request, 'registration/add_attendance.html',context)

    






def give_attendence(classroom_id,rec_subject_id,rec_absent_student_list):
    all_student=Student.objects.filter(s_class=classroom_id)
    all_student_set=set(all_student)
    absent_student_set = set([Student.objects.get(s_id=i) for i in rec_absent_student_list])
    # absent_student_set=set()
    # for i in rec_absent_student_list:
    #     abs_stu=Student.objects.get(s_id=i)
    #     absent_student_set.add(abs_stu)
    # absent_student_set=set(rec_absent_student_list)
    present_student_set=all_student_set-absent_student_set
    for j in present_student_set:
        stosmap=SubtoStudentMap.objects.get(subject=rec_subject_id,student=rec_subject_id)
        stosmap.att_value+=1
        stosmap.save()
        j.s_att+=1
        j.save()
    
def CIA_score(rec_subject_id,rec_student_id,cia_score_list):
    stosmap=SubtoStudentMap.objects.get(subject=rec_student_id,student=rec_student_id)
    stosmap.cia1_score=cia_score_list[0]
    stosmap.cia2_score=cia_score_list[1]
    stosmap.cia3_score=cia_score_list[2]
    stosmap.save()


def MIDSEM_score(rec_subject_id, rec_student_id, midsem_score):
    stosmap = SubtoStudentMap.objects.get(
        subject=rec_student_id, student=rec_student_id)
    stosmap.mid_sem_score=midsem_score
    stosmap.save()


def ENDSEM_score(rec_subject_id, rec_student_id, endsem_score):
    stosmap = SubtoStudentMap.objects.get(
        subject=rec_student_id, student=rec_student_id)
    stosmap.end_sem_score = endsem_score
    stosmap.save()

    

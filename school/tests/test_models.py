from django.test import TestCase
from ..models import *
from datetime import datetime

class Testmodels(TestCase):

    def setUp(self):

        obj_user = User.objects.create_user(username="testusermodel",password="testpasswordmodel",first_name="testmodel",last_name="testlastnamemodel")
        obj_user.save()

        obj_teacher = TeacherExtra(user_id=obj_user.id,salary=10000)
        obj_teacher.save()

        obj_user_student = User.objects.create_user(username="student",password="student",first_name="student",last_name="student")
        obj_user_student.save()

        obj_student = StudentExtra(user_id=obj_user_student.id,roll=10000)
        obj_student.save()




    def test_teacherextramodel(self):

        find_teacher = User.objects.get(username="testusermodel")
        obj_teacher = TeacherExtra.objects.get(user_id=find_teacher.id)
        teacher_namme = find_teacher.first_name + " " +find_teacher.last_name

        self.assertEqual(obj_teacher.__str__(),"testmodel")
        self.assertEqual(obj_teacher.get_id,obj_teacher.user_id)
        self.assertEqual(obj_teacher.get_name,teacher_namme)


    def test_studentextramodel(self):

        find_student = User.objects.get(username="student")
        obj_student = StudentExtra.objects.get(user_id=find_student.id)

        student_name = find_student.first_name + " " + find_student.last_name

        self.assertEqual(obj_student.__str__(),"student")
        self.assertEqual(obj_student.get_id,obj_student.user_id)
        self.assertEqual(obj_student.get_name,student_name)


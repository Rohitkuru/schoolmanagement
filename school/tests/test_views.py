from django.test import TestCase
from django.urls import reverse,resolve
from ..models import User,Attendance,StudentExtra,TeacherExtra


class TestViews(TestCase):

    def setUp(self):
        obj_user = User.objects.create_user(username="testuser",password="testpassword",first_name="test",last_name="testlastname")
        obj_user.save()


    def test_home_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)

    def test_home_view_afterlogin(self):

        user = User.objects.get(username="testuser")
        self.client.force_login(user=user)
        response = self.client.get("/")

        self.assertEqual(response.status_code,302)


    def test_adminclick_view(self):

        response = self.client.get("/adminclick")
        self.assertEqual(response.status_code,200)


    def test_teacherclick_view(self):
        response = self.client.get("/teacherclick")
        self.assertEqual(response.status_code,200)


    def test_studentclick_view(self):
        response = self.client.get("/studentclick")
        self.assertEqual(response.status_code,200)

    def test_aboutus_view(self):
        response = self.client.get("/aboutus")
        self.assertEqual(response.status_code,200)

    def test_contactus_view(self):
        response = self.client.get("/contactus")
        self.assertEqual(response.status_code,200)

    def test_student_signup_get(self):
        response = self.client.get("/studentsignup")
        self.assertEqual(response.status_code,200)


    def test_student_signup_post(self):
        user = User.objects.get(username="testuser")
        data = {
            "first_name": user.first_name,
            "username": user.username,
            "lastname": user.last_name,
            "mobile": "1234567890",
            "cl" : "two",
            "roll" : 2,
            "fee" : 10000
        }

        response = self.client.post("/studentsignup",data=data)
        self.assertEqual(response.status_code,302)


    def test_teacher_sign_up(self):
        user = User.objects.get(username="testuser")
        data = {
            "first_name": user.first_name,
            "username": user.username,
            "lastname": user.last_name,
            "mobile": "1234567890",
            "salary" : 50000
        }

        response = self.client.post("/teachersignup", data=data)
        self.assertEqual(response.status_code, 302)

    def test_admin_sign_up(self):
        user = User.objects.get(username="testuser")
        data = {
            "first_name": user.first_name,
            "username": user.username,
            "lastname": user.last_name,
            "password": user.password
        }

        response = self.client.post("/adminsignup", data=data)
        self.assertEqual(response.status_code, 200)


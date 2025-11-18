from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'student_id', 'date_of_birth']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'coordinator', 'max_students']

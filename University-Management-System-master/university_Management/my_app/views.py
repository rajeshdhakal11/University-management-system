from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm
from django.contrib import messages
#from django.shortcuts import redirect, get_object_or_404
from my_app.models import Course

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Get the selected course ID from the form data
            course_id = request.POST.get('course')
            # Attach the course to the student instance before saving
            student = form.save(commit=False)
            student.course_id = course_id
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    courses = Course.objects.all()  # Fetch all available courses
    return render(request, 'create_student.html', {'form': form, 'courses': courses})




def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def student_detail(request, pk):
    # Retrieve the student object with the given primary key (pk)
    student = get_object_or_404(Student, pk=pk)
    
    # Render the student detail template with the student object
    return render(request, 'student_detail.html', {'student': student})



from .models import Course  # Assuming you have a Course model defined in models.py

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

def delete_course(request, pk):
    # Retrieve the course object to delete
    course = get_object_or_404(Course, pk=pk)
    
    if request.method == 'GET':
        # Display a confirmation page to ensure the user intends to delete the course
        return render(request, 'confirm_course_delete.html', {'course': course})
    elif request.method == 'POST':
        # If the request method is POST, the user confirmed the deletion
        course.delete()
        return redirect('course_list')
    

def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'update_course.html', {'form': form})

def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        # Handle delete logic
        student.delete()
        # Redirect to student list page after deletion
        return redirect('student_list')
    return render(request, 'confirm_student_delete.html', {'student': student, 'student_id': student_id})

def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        # Update student details here
        return redirect('student_list')
    return render(request, 'update_student.html', {'student': student})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})

def home(request):
    return render(request, 'home.html')

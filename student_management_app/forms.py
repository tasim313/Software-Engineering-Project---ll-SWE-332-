from django import forms
from django.forms import ChoiceField
from .models import Courses, Subjects, Students, SessionYearModel


class ChoiceNoValidation(ChoiceField):
    def validate(self, value):
        pass


class DateInput(forms.DateInput):
    input_type = 'date'


class AddStudentForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50,
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control', "autocomplete": "off"}))
    password = forms.CharField(label='Password', max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label="Address", max_length=200,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_list = []

    try:
        courses = Courses.objects.all()
        for course in courses:
            small_course = (course.id, course.course_name)
            course_list.append(small_course)
    except:
        course_list = []

    session_list = []
    try:
        sessions = SessionYearModel.object.all()

        for ses in sessions:
            small_ses = (ses.id, str(ses.session_start_year) + "   TO  " + str(ses.session_end_year))
            session_list.append(small_ses)
    except:
        session_list = []
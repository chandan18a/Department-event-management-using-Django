from django import forms
from betterforms.multiform import MultiModelForm

from .models import Event, EventImage, EventAgenda


class EventForm(forms.ModelForm):


    class Meta:
        model = Event
        fields = ['category', 'name', 'uid', 'description','job_category','scheduled_status','location', 'venue', 'start_date', 'end_date',  'points', 'maximum_attende', 'status']
        widgets = {
            'start_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class EventImageForm(forms.ModelForm):


    class Meta:
        model = EventImage
        fields = ['image']



class EventAgendaForm(forms.ModelForm):


    class Meta:
        model = EventAgenda
        fields = ['session_name', 'speaker_name', 'start_time', 'end_time', 'venue_name']

        widgets = {
            'start_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
        }


class EventCreateMultiForm(MultiModelForm):
    form_classes = {
        'event': EventForm,
        'event_image': EventImageForm,
        'event_agenda': EventAgendaForm,
    }

# events/forms.py
from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, label="Full Name", required=True)
    usn = forms.CharField(max_length=10, label="USN", required=True, help_text="Enter your University Serial Number")
    sem = forms.ChoiceField(choices=[(str(i), f"Semester {i}") for i in range(1, 9)], label="Semester", required=True)
    event_category = forms.ChoiceField(
        choices=[
            ('sports', 'Sports'),
            ('cultural', 'Cultural'),
            ('technical', 'Technical'),
            ('curricular', 'Curricular'),
        ],
        label="Event Category",
        required=True
    )
    event = forms.CharField(max_length=100, label='Event')
    email = forms.EmailField(label="Email", required=True)

    def clean_usn(self):
        usn = self.cleaned_data.get('usn')
        if len(usn) != 10:  # Example validation for USN length
            raise forms.ValidationError("USN must be exactly 10 characters long.")
        return usn

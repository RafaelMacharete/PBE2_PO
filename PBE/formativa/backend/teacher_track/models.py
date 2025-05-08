from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class MyValidator(UnicodeUsernameValidator):
    regex = r'^[\w.@+\- ]+$'

def validate_image_size(image):
    max_size = 1 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError("Imagem size must be lower than 1MB.")

class Account(AbstractUser):
    REQUIRED_FIELDS = ['email', 'nif', 'phone', 'birth_date', 'hire_date', 'name']

    username_validator = MyValidator()
    username = models.CharField(
        _('nif'),
        max_length=10,
        unique=True,
        help_text=_('Required. 10 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
            error_messages={
            'unique': _("A user with that nif already exists."),
        },
    )
    
    name = models.CharField(max_length=100)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='teachers', null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    birth_date = models.DateField()
    hire_date = models.DateField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True, validators=[validate_image_size])

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    responsible_teacher = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='subjects')
    assistant_teacher = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='assistant_subjects', null=True, blank=True)
    course = models.CharField(max_length=100)
    course_load = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Classroom(models.Model):
    period_choices =[
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
    ]

    name = models.CharField(max_length=100, unique=True)
    teacher = models.ManyToManyField(Account, related_name='classrooms')
    subject = models.ManyToManyField(Subject, related_name='classrooms')
    initial_date = models.DateField()
    final_date = models.DateField()
    period = models.CharField(max_length=10, choices=period_choices)
    hours = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
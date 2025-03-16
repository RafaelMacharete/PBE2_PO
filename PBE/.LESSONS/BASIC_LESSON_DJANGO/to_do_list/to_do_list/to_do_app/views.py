from django.shortcuts import render
from .models import Task

# Create your views here.
def list_taks(request):
    tasks = Task.objects.all().order_by('task_status')
    return render(request, 'to_do_list/to_do_list.html', {'tasks': tasks})
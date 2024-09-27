from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from managementapp.models import task_table
from .models import Task, Category


# Create your views here.
def project(request):

    record=task_table.objects.all()
    template= loader.get_template('to_do_list.html')
    context={
        'record': record,
    }
    return HttpResponse(template.render(context,request))


def project_list(request):
    if request.method == 'POST':
        action = request.POST.get('action')  # Get which button was pressed

        if action == 'add':
            # Handle add logic (e.g., render new task form)
            return render(request, 'new_task.html')

        elif action == 'delete':
            # Handle delete logic
            tasks_to_delete = request.POST.getlist('tasks_to_delete')  # Get selected task IDs
            if tasks_to_delete:
                task_table.objects.filter(id__in=tasks_to_delete).delete()  # Delete the selected tasks
                return redirect("managementapp:project")
            else:
                return HttpResponse("No tasks selected for deletion")

        return HttpResponse("Invalid action")
    
    return HttpResponse("Invalid request")


def enter_new_task(request):
    if request.method=='POST':
        task=request.POST.get('task')
        due_date=request.POST.get('due_date')
        new_task=task_table(task=task,due_date=due_date)
        new_task.save()
    return redirect('managementapp:project')

def task_list(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    selected_category = request.GET.get('category', None)
    
    if selected_category:
        tasks = tasks.filter(category__id=selected_category)
    
    return render(request, 'task_list.html', {
        'tasks': tasks,
        'categories': categories,
        'selected_category': selected_category
    })


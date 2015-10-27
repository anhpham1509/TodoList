from django.shortcuts import render
from ToDoListApp.models import Category, Task
from ToDoListApp.forms import CategoryForm, TaskForm


def index(request):
    category_list = Category.objects.all()
    task_list = Task.objects.all()
    context_dict = {'categories': category_list,
                    'tasks': task_list,
                    'category_name_slug': "other",
                    'header': "All",
                    }

    return render(request, 'category.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}

    try:
        category_list = Category.objects.all()
        context_dict['categories'] = category_list
        cat = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = cat.name
        task_list = Task.objects.filter(category=cat)
        context_dict['tasks'] = task_list
        context_dict['category'] = cat
        context_dict['category_name_slug'] = category_name_slug
        context_dict['header'] = cat

    except Category.DoesNotExist:
        pass

    return render(request, 'category.html', context_dict)


def add_category(request):
    category_list = Category.objects.all()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print (form.errors)
    else:
        form = CategoryForm()

    context_dict = {'form': form,
                    'categories': category_list,
                    'header': "Add a Category",
                    }

    return render(request, 'add_category.html', context_dict)


def add_task(request, category_name_slug):
    category_list = Category.objects.all()
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            if cat:
                task = form.save(commit=False)
                task.category = cat
                task.save()
                return category(request, category_name_slug)
        else:
            print (form.errors)
    else:
        form = TaskForm()

    context_dict = {'form': form,
                    'categories': category_list,
                    'category': cat,
                    'category_name_slug': category_name_slug,
                    'header': "Add a Task into " + cat.name,
                    }

    return render(request, 'add_task.html', context_dict)


def test(request):
    category_list = Category.objects.all()
    task_list = Task.objects.all()
    context_dict = {'categories': category_list,
                    'tasks': task_list}

    return render(request, 'base.html', context_dict)
from django import forms
from ToDoListApp.models import Task, Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter new category name")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class TaskForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter new task")
    isFinished = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    deadline = forms.DateField(help_text="Deadline")

    class Meta:
        model = Task
        exclude = ('category',)
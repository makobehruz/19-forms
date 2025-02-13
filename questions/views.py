from django.shortcuts import render, redirect, get_object_or_404

from .models import Test
from .forms import TestForm, Question


def home(request):
    return render(request,'index.html')

def test_list(request):
    tests = Test.objects.all()
    ctx = {'tests': tests}
    return render(request,'questions/test-list.html', ctx)


def test_create(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save()
            questions = request.POST.getlist('questions[]')
            answers1 = request.POST.getlist('answers1[]')
            answers2 = request.POST.getlist('answers2[]')
            for q, a1, a2 in zip(questions, answers1, answers2):
                Question.objects.create(
                    test=test,
                    question=q,
                    answer1=a1,
                    answer2=a2
                )
            return redirect('questions:list')
    else:
        form = TestForm()
    ctx = {'form': form}
    return render(request, 'questions/test-formset.html', ctx)

def test_delete(request, pk):
    test = get_object_or_404(Test, pk=pk)
    if request.method == 'POST':
        test.delete()
        return redirect('questions:list')
    return render(request, 'questions/delete.html', {'test': test})


def test_edit(request, pk):
    test = get_object_or_404(Test, pk=pk)
    if request.method == 'POST':
        form = TestForm(request.POST, instance=test)
        if form.is_valid():
            test = form.save()
            test.questions.all().delete()
            questions = request.POST.getlist('questions[]')
            answers1 = request.POST.getlist('answers1[]')
            answers2 = request.POST.getlist('answers2[]')
            for q, a1, a2 in zip(questions, answers1, answers2):
                Question.objects.create(
                    test=test,
                    question=q,
                    answer1=a1,
                    answer2=a2
                )
            return redirect('questions:list')
    else:
        form = TestForm(instance=test)
    ctx = {
        'form': form,
        'test': test,
        'questions': test.questions.all(),
    }
    return render(request, 'questions/test-formset.html', ctx)
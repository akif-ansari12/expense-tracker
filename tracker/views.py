from django.shortcuts import render, redirect
from .models import Expense
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



@login_required
def home(request):
    expenses = Expense.objects.filter(user=request.user)

    total = sum(e.amount for e in expenses)

    #SMART INSIGHT
    category_total = {}
    for e in expenses:
        category_total[e.category] = category_total.get(e.category, 0) + e.amount

    insight = ""
    if category_total:
        max_category = max(category_total, key=category_total.get)
        insight = f"You are spending too much on {max_category}"

    return render(request, 'home.html', {
        'expenses': expenses,
        'total': total,
        'insight': insight,
        'category_total': category_total,
    })
@login_required
def add_expense(request):
    if request.method=="POST":
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        note = request.POST.get('note')

        Expense.objects.create(
          user=request.user,
          amount=amount,
          category=category,
          note=note
        )
        return redirect('/')
    
    return render(request, 'add.html')

@login_required
def delete_expense(request, id):
    exp = Expense.objects.get(id=id)
    exp.delete()
    return redirect('/')


@login_required
def edit_expense(request, id):
    exp = Expense.objects.get(id=id)

    if request.method == 'POST':
        exp.amount = request.POST.get('amount')
        exp.category = request.POST.get('category')
        exp.note = request.POST.get('note')
        exp.save()
        return redirect('/')
    
    return render(request, 'edit.html', {'exp':exp})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')   # signup ke baad login page
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})






    



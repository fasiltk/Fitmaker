from django.shortcuts import render, HttpResponse, redirect
from .models import Product
from django.contrib import messages
import pandas as pd

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['username'] = username
        request.session['password'] = password


        try:
            user = Product.objects.get(username=username, password=password)
            request.session['logged_in_username'] = username
            return redirect('inputpage')
        except Product.DoesNotExist:
            messages.error(request, "Invalid username or password")
    return render(request, "index.html")

def registers(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        name=request.POST.get('name')
        phonenumber=request.POST.get('phonenumber')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        if len(password) < 8:
            messages.error(request, "Password should be at least 8 characters long")
        fm=Product(username=username,password=password,name=name,phonenumber=phonenumber,age=age,gender=gender)
        fm.save()
        return redirect('index')
    return render(request,"registers.html")
def input_page_view(request):
    username = "test_username"  # Hardcoded for testing
    return render(request, 'simple_test_template.html', {'username': username})

def session_test_view(request):
    username = request.session.get('logged_in_username')
    return HttpResponse(f"Username from session: {username}")

def inputpage(request):
    username = request.session.get('logged_in_username')
    if username:
        if request.method == 'POST':
            weight = request.POST.get('weight')
            height = request.POST.get('height')

            # Get dynamic food items and quantities
            food_items = request.POST.getlist('fooditem[]')
            quantities = request.POST.getlist('quantity[]')
            username = request.session.get('username', None)


        # Store input data in session
            request.session['user_weight'] = weight
            request.session['user_height'] = height
            request.session['user_fooditems'] = food_items
            request.session['user_quantities'] = quantities
            return redirect('outputpage')
        product_instance = Product.objects.get(username=username)
        print(product_instance.name)
        return render(request, "inputpage.html", {'username': product_instance.name})
    else:
        return redirect('index')

def outputpage(request):
    user_weight = request.session.get('user_weight', None)
    user_height = request.session.get('user_height', None)
    user_fooditems = request.session.get('user_fooditems', [])
    user_quantities = request.session.get('user_quantities', [])

    total_cal = []
    df = pd.read_csv('static/data/calories.csv')
    total = 0

    for food, qnty in zip(user_fooditems, user_quantities):
        cal = int(df.loc[df['FoodItem'] == food]['Cals_per100grams'].values)
        calories = int(cal) * int(qnty)
        total += calories
        total_cal.append(calories)

    ex = pd.read_csv('static/data/exercise_dataset.csv')
    ex1 = []
    ex2 = []
    ex3 = []
    ex4 = []
    i = []
    j = []
    k = []
    l = []

    if int(user_weight) >= 92.9:
        ex1 = ex.loc[ex['205 lb'] <= total]['Activity, Exercise or Sport (1 hour)'].values
        ex11 = ex.loc[ex['205 lb'] <= total]['205 lb'].values
        for x in ex11:
            a = round(total / x,2)
            i.append(a)
        ex1, i = zip(*sorted(zip(ex1, i), key=lambda x: x[1]))
    elif int(user_weight) >= 81.6:
        ex2 = ex.loc[ex['180 lb'] <= total]['Activity, Exercise or Sport (1 hour)'].values
        ex22 = ex.loc[ex['180 lb'] <= total]['180 lb'].values
        for y in ex22:
            b = round(total / y,2)
            j.append(b)
        ex2, j = zip(*sorted(zip(ex2, j), key=lambda x: x[1]))
    elif int(user_weight) >= 70.3:
        ex3 = ex.loc[ex['155 lb'] <= total]['Activity, Exercise or Sport (1 hour)'].values
        ex33 = ex.loc[ex['155 lb'] <= total]['155 lb'].values
        for z in ex33:
            c = round(total / z,2)
            k.append(c)
        ex3, k = zip(*sorted(zip(ex3, k), key=lambda x: x[1]))
    elif int(user_weight) < 70.3:
        ex4 = ex.loc[ex['130 lb'] <= total]['Activity, Exercise or Sport (1 hour)'].values
        ex44 = ex.loc[ex['130 lb'] <= total]['130 lb'].values
        for zz in ex44:
            d = round(total / zz,2)
            l.append(d)
        ex4, l = zip(*sorted(zip(ex4, l), key=lambda x: x[1]))



    context = {
        'user_weight': user_weight,
        'user_height': user_height,
        'user_data': zip(user_fooditems, user_quantities, total_cal),
        'total': total,
        'ex1': zip(ex1, i),
        'ex2': zip(ex2, j),
        'ex3': zip(ex3,k),
        'ex4': zip(ex4,l)
    }

    return render(request, "outputpage.html", context)
def change_password(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        new_password = request.POST.get('new_password', None)

        # Update the password for the user with the new password
        Product.objects.filter(username=username).update(password=new_password)
        

        return redirect('index')  # Redirect to the desired page after changing the password

    return render(request, "change_password.html")
def logout_view(request):
   request.session.flush()
   return redirect('index')
def diseases(request):
    if request.method=='POST':
        diseases=request.POST.get('diseases')
        request.session['diseases']=diseases
        measurement=request.POST.get('measurement')
        request.session['measurement']=measurement
        if diseases=='Diabetes':
            return redirect('Diabetes')
        elif diseases=='Cholesterol':
            return redirect('Cholesterol')
        elif diseases=='BloodPressure':
            return redirect('BloodPressure')
    return render(request,"diseases.html")
def Diabetes(request):
    user_measurement= request.session.get('measurement')
    return render(request,"Diabetes.html",{'user_measurement':user_measurement})
def Cholesterol(request):
    user_measurement= request.session.get('measurement')
    return render(request,"Cholesterol.html",{'user_measurement':user_measurement})
def BloodPressure(request):
    user_measurement= request.session.get('measurement')
    return render(request,"BloodPressure.html",{'user_measurement':user_measurement})
def patients(request):
    if request.method == 'POST':
        patients = request.POST.get('patients')
        request.session['patients'] = patients
        if patients == 'heart':
            return redirect('heart')
        elif patients == 'disc':
            return redirect('disc')
        elif patients == 'kidney':
            return redirect('kidney')
        elif patients == 'backbone':
            return redirect('backbone')
    return render(request, "patients.html")

def heart(request):
    return render(request,"heart.html")
def disc(request):
    return render(request,"disc.html")
def kidney(request):
    return render(request,"kidney.html")
def backbone(request):
    return render(request,"backbone.html")
def demo(request):
    return render(request,"demo.html")
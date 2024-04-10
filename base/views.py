from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context={}
    return render(request,'base/calculator.html',context)

def calculate(request):
    if request.method == 'POST':
        number_one = request.POST.get("num1")
        number_two = request.POST.get("num2")
        operation = request.POST.get("operator")
        if operation == "+":
            result = float(number_one) + float(number_two)
        elif operation == "-":
            result = float(number_one) - float(number_two)
        elif operation == "*":
            result = float(number_one) * float(number_two)
        elif operation == "/":
            if float(number_two) != 0:
                result = float(number_one) / float(number_two)
            else:
                return render(request, "base/calculator.html", {'error': "Cannot divide by zero."})
        else:
            return render(request, "base/calculator.html", {'error': "Invalid operation."})
        context = {'result': result}
        return render(request, "base/calculator.html", context)
    else:
        return render(request, "base/calculator.html")

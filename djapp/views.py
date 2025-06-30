from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hi this is eshwar!...")

def demo(request):
    output=""
    if request.method=="POST":
        num1=int(request.POST.get("fn"))
        num2=int(request.POST.get("sn"))
        opr=request.POST.get("opr")
        if opr=='+': 
            output =num1+num2
        elif opr=='-':
            output=num1-num2
        elif opr=='*':
            output=num1*num2
        elif opr=='/':
            output=num1/num2
    return render(request,"forms.html",{'o':output})
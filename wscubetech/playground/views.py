from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    data = {
        "title": "My Home",
        "clist": ["PHP", "JAVA", "c", "c++"],
        'number': [10,20,19, 2],
        "student_details": [
            {"name": "name1", "email": "email1@gmail.com"},
            {"name": "name2", "email": "email2@gmail.com"},
            {"name": "name3", "email": "email3@gmail.com"},
            {"name": "name4", "email": "email4@gmail.com"},
            
        ]
    }
    return render(request, "index.html", data)


def About(request):
    return HttpResponse("hello there!")


def courseDetails(request, courseId):
    # here courseId is the variable that stores any parameter whch is passed in the url of the site.
    return HttpResponse(courseId)

def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=='+':
                c=n1+n2
            elif opr=='-':
                c=n1-n2
            elif opr=='*':
                c=n1*n2
            else:
                c=n1/n2    
            
    except:
        c="Invalid operator...."
    print(c)
    return render(request,"calculator.html",{'c':c})
from django.http import HttpResponse
from django.shortcuts import render
from conversion import taking_content, transfering_content

def expertIMP(request):
    d = {}
    try:
        if request.method == "POST":
            n1 = request.POST['takingcode']
            with open("data_extract.txt", 'w') as f:
                f.writelines(n1)
            
            x, _ = taking_content()
            transfering_content(x)
            
            with open("data_converted.txt", 'r') as f:
                line = f.read()
                d = {'n1': n1, 'output': line}
                return render(request, "index.html", d)
    except Exception as e:
        print(e)

    return render(request, "index.html", d)

def aboutUS(request):
    return render(request, "about-us.html")

def studyMAT(request):
    return render(request, "study-material.html")
from django.shortcuts import render

# Create your views here.
def project_one(request):
    return render(request,'project_one.html')


def project_two(request):
    return render(request,'project_two.html')
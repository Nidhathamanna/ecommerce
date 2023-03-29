from django.shortcuts import render

# Create your views here.
def c_home(request):
    return render(request,'ecomadmin/ecomadmin.html')

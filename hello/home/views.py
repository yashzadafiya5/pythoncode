from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,"index.html")
    # return HttpResponse("this is a home page")
def about(request):
    return render(request,"about.html")
    # return HttpResponse("this is a about page")
def contect_us(request):
    return render(request,"contect_us.html")
    # return HttpResponse("this is a contect_us page")
def services(request):
    return render(request,"services.html")
    # return HttpResponse("this is a service page")

# Create your views here.

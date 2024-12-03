from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'virat kohli','age':35,'centuries':81}
    return render(request,'jinja_print.html',context=d)
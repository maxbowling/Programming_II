from django.shortcuts import render

# Create your views here.
def home(request):
    name=request.GET.get('name','')
    name_list=[name,name[::-1]]
    return render(request,'lab10_app/home.html',{'name':name_list})


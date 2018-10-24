from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request): 
    return render(request,'app_01/index.html')

def process(request):
    if request.method != "POST":
        return redirect('/')
    if request.method =="POST":
        request.session['q0']=request.POST['q0']
        request.session['q1']=request.POST['q1']
        request.session['q2']=request.POST['q2']
        request.session['q3']=request.POST['q3']
    if 'cnt' not in request.session:
        request.session['cnt']=0
    else:
        request.session['cnt']=request.session['cnt']+1
    return redirect('/submitted')        

def submitted(request):
    return render(request,'app_01/submitted.html')      
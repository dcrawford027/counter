from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    if 'visited' not in request.session:
        request.session['visited'] = 1
    else:
        request.session['visited'] += 1
    return render(request, 'index.html')

def destroySession(request):
    del request.session['counter']
    del request.session['visited']
    return redirect('/')

def increaseByTwo(request):
    request.session['counter'] += 1
    return redirect('/')

def chooseIncrement(request):
    print(request.POST)
    num = request.POST['incNum']
    request.session['counter'] += int(num) - 1
    return redirect('/')
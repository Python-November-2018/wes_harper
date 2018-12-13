from django.shortcuts import render, redirect

# Create your views here.
def index(request):
  return render(request, 'first_app/index.html')

def process(req):
  print("*" * 80)
  print(req.POST['name'])
  return redirect('/')
from django.shortcuts import render

# Create your views here.
def throw(requests):
  context={
    'name':'minhwan'
  }
  return render(requests,'firstapp/throw.html',context)

def catch(requests):
  print(requests.GET.get('name'))
  print(requests.GET.get('massage'))
  name=requests.GET.get('name')
  massage=requests.GET.get('massage')
  context={
    'name':name,
    'massage':massage,
  }
  return render(requests,'firstapp/catch.html',context)
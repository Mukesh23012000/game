from django.shortcuts import render,HttpResponse

def strike(name1,name2):
  name2 = list(name2)
  temp = str()
  for i in name1:
    if i in name2:
      name2.remove(i)
    else:
      temp = temp+i
  count = len(temp)+len(name2)
  c = output(count)
  return c
def output(count):
  flames = ['Friends😎','Love💕','Affection🥰','Marriage👩‍❤️‍👨','Enemy😈','Sister/Brother💞']
  while(len(flames)>1):
    temp_flames=flames*50
    c = temp_flames[count]
    flames.remove(c)
  c = last(flames[0])
  return c
def last(l):
  c =  l
  return c

def index(request):
    c = str()
    r=str()
    if request.method == "POST":
        name1 = request.POST["name1"]
        name2 = request.POST["name2"]
        print(name1)
        print(name2)
        n1=name1.capitalize()
        n2 = name2.capitalize()
        c = n1+ " and "+n2+" are "
        r = strike(name1,name2)
    return render(request,"index.html",{'text':c,'answer':r})
    

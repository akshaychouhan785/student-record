from django.shortcuts import render, redirect

from .models import Student

def index(request):
	stud=Student.objects.all()
	return render(request, 'index.html', {'students':stud})

def addstudent(request):
 if request.method=='POST':
		s=Student()
		s.stu_name=request.POST['stu_name']
		s.email=request.POST['email']
		s.mobile=request.POST['mobile']
		s.address=request.POST['address']
		s.branch=request.POST['branch']
		s.year=request.POST['year']
		s.semester=request.POST['semester']
		o=request.POST['honors']
		if o=="on":
			s.honors=True
		else:
			s.honors=False
		s.save()
		return redirect("/")
 else:
   return render(request, 'addstudent.html')

def delete(request):
    id=request.GET['id']
    id=int(id)
    s=Student()
    s.id=id
    s.delete()
    return redirect("/")

    
def update(request):

    if request.method=='POST':
        s=Student()
        s.id=request.POST['id']
        s.stu_name=request.POST['stu_name']
        s.email=request.POST['email']
        s.mobile=request.POST['mobile']
        s.address=request.POST['address']
        s.branch=request.POST['branch']
        s.year=request.POST['year']
        s.semester=request.POST['semester']
        s.honors=request.POST['honors']
        s.save()
        return redirect('/')

    else:
        id=request.GET['id']
        s=Student.objects.filter(id=id).get()
        return render(request, 'update.html', {'stud':s})  
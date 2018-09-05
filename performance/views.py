from django.shortcuts import render
from performance.models import AddEmployee,FeedbackForm
import datetime
# Create your views here.

def login(request):
	if request.method == 'POST':
		msg=""
		val=request.POST['email'] 
		pwd=request.POST['pass']
		try:
			red=AddEmployee.objects.filter(mailid=val)
			if red:	
				if red[0].password==pwd:
					print("4")
					request.session['userid'] = val	
					x=AddEmployee.objects.all()
					return render(request,'index2.html',{"x":x})
				else:
					print("3")
					m="Not Matched forgotten your password"
					return render(request, 'index.html',{"m":m})
						
			else:
				print("2")
				m="could not found your account"
				return render(request, 'index.html',{"m":m})		
		except:
			print("1")
			return redirect('/login/')
	else:
		return render(request, 'index.html');

def feedback(request):
	if request.method == 'POST':
		empid=request.POST['empid'] 
		feedback=request.POST['feedback']
		today = datetime.datetime.today()
		sender=	request.session['userid'] 
		obj=FeedbackForm(employeeid=empid,reviewer=sender,date=today,feedback=feedback)
		obj.save()
		x=AddEmployee.objects.all()
		return render(request,'index2.html',{"x":x})
	else:
		empid=request.GET['queryname']
		return render(request, 'index3.html',{"empid":empid});

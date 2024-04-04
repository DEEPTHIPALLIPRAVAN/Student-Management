from django.shortcuts import render,redirect
from django.http import HttpResponse
# from app.models import Fileupload
from app.models import User,Student,Teacher
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# # Create your views here.
def nav(request):
    return render(request,'nav.html')

def sthome(request):
     return render(request,'studenthme.html')
def stutchview(request):
     y=Teacher.objects.all()
     return render(request,'stutchview.html',{'data':y})

def stuprofedit(request):
     sessn=request.session['st_id']
     print(sessn)
     st=Student.objects.get(S_id=sessn) 
     us=User.objects.get(id=sessn)
     return render(request,'stuprofileedit.html',{'stud':st,'use':us})

def studprofupdate(request):
     if request.method=='POST':
          ses=request.session['st_id']
          print(ses)
          name=request.POST['name']
          dob=request.POST['dob']
          mobilenum=request.POST['mobilenumber']
          gen=request.POST['gender']
          S_id=request.POST['S_id']
          print(S_id)
          user=request.POST['username']
          edit=Student.objects.get(S_id=ses)
          ed=User.objects.get(id=ses)
          edit.Name=name
          edit.DOB=dob
          edit.MobileNumber=mobilenum
          edit.Gender=gen
          edit.save()
          ed.username=user
          ed.save()
          return redirect(sthome)


def adminhome(request):
     return render(request,'adminhome.html')

def teacherhome(request):
     return render(request,'teacherhome.html')

def teacherprofile(request):
     sessn=request.session['te_id']
     t=Teacher.objects.get(T_id=sessn)
     u=User.objects.get(id=sessn)
     return render(request,'teacherprof.html',{'teach':t,'us':u})
     
     

def user_log(request):
     if request.method=='POST':
          username=request.POST.get('username')
            
          passwd=request.POST.get('password')
          user= authenticate(request,username=username,password=passwd)
      


          if user is not None and user.is_superuser==1:
               login(request,user)
               return render(request,'adminhome.html')
            
          elif user is not None and user.usertype=='Student':
               login(request,user)
               stu = Student.objects.get(S_id = user.id)
               print(stu)
               request.session['st_id']=stu.S_id.id
               return render(request,'studenthme.html')
            
          elif user is not None and user.usertype=='Teacher':
               login(request,user)
               tea=Teacher.objects.get(T_id=user.id)

               request.session['te_id']=tea.T_id.id

               return redirect(teacherhome)
                 
          else:
               return HttpResponse("invalid details")

     else:
          return render(request,'indexlog.html')

      

def addteacher(request):
    
        if request.method=='POST':
            fname=request.POST['Name']
            dpt=request.POST['dept']
            usrname=request.POST['username']
            exp=request.POST['exp']
            password=request.POST['password']
            cnf=request.POST['confirmpassword']
            age=request.POST['age']
            Email=request.POST['email']
            ph=request.POST['ph_no']

            x=User.objects.create_user(password=password,username=usrname,email=Email,usertype='Teacher')
            Teacher.objects.create(Name=fname,Phone_Number=ph,ConfirmPassword=cnf,Department=dpt,Age=age,Experience=exp,T_id=x)
            return redirect(adminhome)
        else:
             return render(request,'indextchr.html')
        
def teacherview(request):
     x=Teacher.objects.all()
     return render(request,'viewteacher.html',{'text':x})

def deleteteacher(request,id):
     t=User.objects.get(id=id)
     t.delete()
     return redirect(teacherview)

def editteacher(request,tt):
     y=Teacher.objects.get(id=tt)
     return render(request,'edittchr.html',{'text':y})
def updateteacher(request,tt):
     if request.method=='POST':
          Name=request.POST['Name']
          Phone_Number=request.POST['ph_no']
          Department=request.POST['dept']
          Experience=request.POST['exp']
          us=request.POST['username']
          print(Phone_Number)
          x=User.objects.get(id=tt)         
          y=Teacher.objects.get(T_id=x)
          print(y)
          x.username=us
          y.Name=Name
          y.Phone_Number=Phone_Number
          y.Department=Department
          y.Experience=Experience
          y.save()
          x.save()
          return redirect(teacherview)
     

            
def studregister(request):
    if request.method=='POST':
        fn=request.POST['NAME']
        Dob=request.POST['DOB']
        Email=request.POST['EMAIL']
        Ph_no=request.POST['Ph_no']
        Gender=request.POST['GENDER']
        usr=request.POST['usr']
        pswd=request.POST['pswd']
        cnf=request.POST['cnfrmpswd']

        y=User.objects.create_user(username=usr,password=pswd,email=Email,usertype='Student')
        Student.objects.create(Name=fn,Conf_pswd=cnf,MobileNumber=Ph_no,Gender=Gender,DOB=Dob,S_id=y)
        return redirect(user_log)
    else:
        return render(request,'indexstreg.html')
    
def studentview(request):
     a=Student.objects.all()
     return render(request,'viewstudent.html',{'data':a})

def deletestudent(request,id):
     s=User.objects.get(id=id)
     s.delete()
     return redirect(studentview)

def editstudent(request,ss):
     x=Student.objects.get(id=ss)
     return render(request,'editstudent.html',{'data':x})

def updatestudent(request,ss):
     if request.method=='POST':
          Name=request.POST['Name']
          Dob=request.POST['DOB']
          MobileNumber=request.POST['MobileNumber']
          Gender=request.POST['Gender']
          usr=request.POST['username']
          m=User.objects.get(id=ss)
          x=Student.objects.get(S_id=m)
          x.Name=Name
          x.DOB=Dob
          x.MobileNumber=MobileNumber
          x.Gender=Gender
          m.username=usr
          x.save()
          m.save()

          return redirect(studentview)

def logouts(request):
     logout(request)
     return redirect(user_log)











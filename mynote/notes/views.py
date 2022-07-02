from django.shortcuts import render
from .models import Notes,UserAccount
from .forms import NotesForm,LoginForm,SignUpForm,SignupImageForm
from django.http import JsonResponse,HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        n=Notes.objects.filter(user=request.user.id)
        # print(n)
        nf=NotesForm()
        ua=list(UserAccount.objects.filter(user=request.user).values())
        if ua:
            print(list(ua))
            l=list(ua)
            print(l[0]['image'])
            return render(request,'notes/index.html',{'n':n,'nf':nf,'ua':ua,'l':l[0]['image']})
        else:
            l=None
            return render(request,'notes/index.html',{'n':n,'nf':nf,'ua':ua})
    else:
        return HttpResponseRedirect('/signin/')

def flash(request):
    return render(request,'notes/flash.html',{})

def sign_in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            uname=request.POST.get('user')
            passw=request.POST.get('pass')
            if uname!="" and passw!="":
                # print(uname)
                # print(passw)
                user=authenticate(username=uname,password=passw)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/home/')
                else:
                    messages.error(request,'Wrong Username or Password')
                    return render(request,'notes/signin.html',{})



            else:
                return render(request,'notes/signin.html',{})
        else:
            return render(request,'notes/signin.html',{})
    else:
        return HttpResponseRedirect('/home/')
                

    

def sign_up(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=SignUpForm(request.POST)
            form1=SignupImageForm(request.POST,request.FILES)
            if form.is_valid() and form1.is_valid():
                user=form.cleaned_data['username']
                img=form1.cleaned_data['image']
                # print(img)
                form.save()
                ua=UserAccount(user=user,image=img)
                ua.save()
                return HttpResponseRedirect('/signin/')
        else:
            form=SignUpForm()
            form1=SignupImageForm()
        return render(request,'notes/signup.html',{'form':form,'form1':form1})
    else:
        return HttpResponseRedirect('/home/')

def addnote(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            nf = NotesForm(request.POST,request.FILES)
            if nf.is_valid():
                nf.save()
                messages.success(request,'Your note created successfully')
                
                return JsonResponse({'status':'saved'})
        else:
            return JsonResponse({'msg':'Not allowed'})
    else:
        return HttpResponseRedirect('/signin/')
                
                
        

       
                
                
                
            

        

            
            

           
def deletenote(request):
    if request.method=='POST':
        id=request.POST.get('id')
        print(id)
        n=Notes.objects.get(pk=id)
        n.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

def edit_note(request):
    if request.method=='POST':
        nid=request.POST.get('notes_id')
        print(nid)
        id=request.POST.get('user_name_id')
        print(id)
        note=request.POST.get('note_modal')
        print(note)
        img=request.FILES.get('file_modal')
        print(img)
        ci=request.POST.get('current_image')
        print(ci)
        print(ci[15:])


        
        p=Notes.objects.get(id=nid)
        p.user=id
        p.note=note
        if img is None:
            pass
        else:
            p.image=img
        
        p.save()

        return JsonResponse({'msg':'updated'})
    

                
   
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/signin/')




     
    

    



    
        
            
    
   
    


    

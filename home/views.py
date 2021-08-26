from home.forms import SearchForm
from django.shortcuts import render,HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import json
from home.forms import SearchForm
from home.models import SchoolSetting, ContactMessage, ContactForm,Post,Teacher,Student, Admins
# Create your views here.
def index(request):
    setting = SchoolSetting.objects.all()
    post = Post.objects.all().order_by('id')[:4]#id birinchi kirgan id bo'yicha taxlaydi
    post_latest = Post.objects.all().order_by('-id')[:4]#oxirgi kiritilgan id bo'yicha
    post_picked = Post.objects.all().order_by('?')[:4]#random holatda
    page = "home"
    context = {
        'setting':setting,
        'page':page,
        'post':post,
        'post_latest':post_latest,
        'post_picked':post_picked,
    }
    return render(request,'index.html',context)

def aboutus(request):
    setting = SchoolSetting.objects.all()
    admins = Admins.objects.all().order_by('id')[:4]
    return render(request,'about.html',{'setting':setting,'admins':admins})

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)#formaga ma'lumot kiritila boshlashi bilan ishlash holati
        if form.is_valid():#ma'lumotlarni tekshirib keyin o'tqizish
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()#jo'natish knopkasi bosilganda ma'lumotlarni tekshirishga tashiymiz,va bazada saqlaydi
            messages.success(request,'Sizning xabaringiz yuborildi, Rahmat!')
            return HttpResponseRedirect('/contact/') #'127.0.0.1:8000'
    setting = SchoolSetting.objects.all()
    form = ContactForm#bu contact formani o'zini chaqiradi,contact pageda
    context = {'setting':setting,'form':form}
    return render(request,'contact.html',context)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            post = Post.object.filter(title__icontains = query)
            teacher = Teacher.objects.filter(name__icontains=query)
            student = Student.objects.filter(name__icontains=query)
            admins = Admins.objects.filter(name__icontains=query)
            context = {
                'query':query,
                'post':post,
                'teacher':teacher,
                'student':student,
                'admins':admins,
            }
            return render(request,'search.html',context)
    return HttpResponseRedirect('/')
def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term','')
        post = Post.object.filter(title__icontains = q)
        teacher = Teacher.objects.filter(name__icontains=q)
        student = Student.objects.filter(name__icontains=q)
        admins = Admins.objects.filter(name__icontains=q)
        result = []
        for rs in post,teacher,student,admins:
            post_json = {}
            post_json = rs.title
            teacher_json = {}
            teacher_json = rs.name
            student_json = {}
            student_json = rs.name
            admins_json = {}
            admins_json = rs.name
            result.append(post_json,teacher_json,student_json,admins_json)
        data = json.dumps(result)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)
def post_detail(request,id):
    post = Post.objects.get(pk=id)
    # images = Post.objects.filter(post_id=id)
    context = {
        'post':post,
        #'images':images,
    }
    return render(request,'post_detail.html',context)
def teacher(request):
    teachers = Teacher.objects.all().order_by('id')[:16]
    return render(request,'teachers.html',{'teachers':teachers})

def student(request):
    students = Student.objects.all().order_by('id')[:16]
    return render(request,'students.html',{'students':students})


def teacher_detail(request,id):
    teachers = Teacher.objects.get(pk=id)
    post = Post.objects.all().order_by('id')[:4]
    context = {
       'teachers':teachers,
       'post':post,
    }
    return render(request,'teacher_detail.html',context)
def student_detail(request,id):
    student = Student.objects.get(pk=id)
    post = Post.objects.all().order_by('id')[:4]
    context = {
       'student':student,
       'post':post,
    }
    return render(request,'student_detail.html',context)

def admins(request):
    admin = Admins.objects.all().order_by('id')[:16]
    return render(request,'admins.html',{'admin':admin})


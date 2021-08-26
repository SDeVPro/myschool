from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea, EmailInput
from django.utils.safestring import mark_safe
# Create your models here.

class SchoolSetting(models.Model):
    title = models.CharField(max_length=222)#maktab nomi 3,4,5,6,7
    keywords = models.CharField(max_length=222)
    description = models.CharField(max_length=222)
    aboutus = RichTextUploadingField()
    contactus = RichTextUploadingField()
    facebook = models.CharField(max_length=222,blank=True)
    instagram = models.CharField(max_length=222,blank=True)
    email = models.EmailField(max_length=222,blank=True)
    tiktok = models.CharField(max_length=222,blank=True)
    youtube = models.CharField(max_length=222,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'setting'
        verbose_name_plural = 'settings'
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=222,blank=True)
    keywords = models.CharField(max_length=222,blank=True)
    description = models.CharField(max_length=222,blank=True)
    detail = RichTextUploadingField()
    image = models.ImageField(upload_to='images')
    author = models.CharField(max_length=222,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))
    image_tag.short_description = 'image'

class Teacher(models.Model):
    name = models.CharField(max_length=222,blank=True)
    surname = models.CharField(max_length=222,blank=True)
    lastname = models.CharField(max_length=222,blank=True)
    subject = models.CharField(max_length=222,blank=True)
    level = models.CharField(max_length=222,blank=True)
    level_years = models.IntegerField()
    image = models.ImageField(upload_to='images')
    classes = models.CharField(max_length=222,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name+" "+self.surname+" "+self.lastname

class Student(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    name = models.CharField(max_length=222,blank=True)
    surname = models.CharField(max_length=222,blank=True)
    lastname = models.CharField(max_length=222,blank=True)
    subject = models.CharField(max_length=222,blank=True)
    level = models.CharField(max_length=222,blank=True,help_text='nechanchi sinf')
    level_years = models.IntegerField()
    image = models.ImageField(upload_to='images')
    classes = models.CharField(max_length=222,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name+" "+self.surname+" "+self.lastname

class ContactMessage(models.Model):
    STATUS = (
        ('New','Yangi'),
        ('Read','Uqildi'),
        ('Closed','Yopilgan'),
    )
    name = models.CharField(blank=True,max_length=222)
    email = models.EmailField(blank=True,max_length=222)
    subject = models.TextField(blank=True,max_length=222)
    message = models.TextField(blank=True,max_length=1000)
    status = models.CharField(max_length=15,default='New',choices=STATUS)
    ip = models.CharField(blank=True,max_length=222)
    note = models.CharField(blank=True,max_length=222)#adminstrator tomonidan kelib tushgan murojaatga munosabati so'zlarda 
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email','subject','message']
        widgets = {
            'name':TextInput(attrs={'class':'input','placeholder':'Name&Surname'}),
            'subject':TextInput(attrs={'class':'input','placeholder':'Subject'}),
            'email':EmailInput(attrs={'class':'input','placeholder':'Email Address'}),
            'message':TextInput(attrs={'class':'input','placeholder':'Your message here','rows':'5'}),
        }

class Admins(models.Model):
    LEVEL = (
        ('Director','Direktor'),
        ('Zauch','Zauch'),
        ('Zamdirektor','Zamdirektor'),
        ('Zavhoz','Zavhoz'),
    )
    CLASSES  = (
        ('1 a','1 a'),
        ('1 b','1 b'),
        ('1 v','1 v'),
        ('1 g','1 g'),
        ('2 a','2 a'),
        ('2 b','2 b'),
        ('2 v','2 v'),
        ('2 g','2 g'),

    )
    name = models.CharField(max_length=222,blank=True)
    surname = models.CharField(max_length=222,blank=True)
    lastname = models.CharField(max_length=222,blank=True)
    subject = models.CharField(max_length=222,blank=True)
    level = models.CharField(max_length=222,blank=True,choices=LEVEL)
    level_years = models.IntegerField()
    image = models.ImageField(upload_to='images')
    classes = models.CharField(max_length=222,blank=True,choices=CLASSES)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name+" "+self.surname+" "+self.lastname
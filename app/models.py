from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField


class SliderImage(models.Model):
    image = models.ImageField(upload_to='sliderimage/')
    discriptions = RichTextField(null=True, blank=True ,default=None)

    class Meta:
        ordering =['id']
        verbose_name = "Slider Image"
        verbose_name_plural = "Slider Images"


class AboutUs(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='aboutimages/')
    discriptions = RichTextField()

    class Meta:
        ordering =['-id']
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.title
    


    

class Testimonials(models.Model):
    full_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='testimonialsimage/')
    discriptions = models.TextField()


    class Meta:
        ordering = ['-id',]
        verbose_name = "Testimonials"
        verbose_name_plural = "Testimonials"
    

    def __str__(self):
        return self.full_name
    

class Frequently_Asked_Question(models.Model):
    title = models.CharField(max_length=250)
    discriptions = RichTextField()

    class Meta:
        ordering =['-id']
        verbose_name = "faq"
        verbose_name_plural = "faqs"

    def __str__(self):
        return self.title
    

class Contact_Info(models.Model):
    phone_number = models.PositiveIntegerField()
    email = models.EmailField()
    location = models.TextField()
    map_url = models.URLField(null=True, blank=True)
    facebook_page_link = models.URLField(null=True, blank=True)
    insta_page_link = models.URLField(null=True, blank=True)
    website_link = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['-id',]
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"
    
class HeadOffice(models.Model):
    contact = models.ForeignKey(Contact_Info, on_delete=models.CASCADE, related_name='contact_informations')
    location = models.TextField()
    phone_number = models.TextField()

    class Meta:
        ordering = ['-id',]
        verbose_name = "Head Office"
        verbose_name_plural = "Head Office"


class BranchOffice(models.Model):
    contact = models.ForeignKey(Contact_Info, on_delete=models.CASCADE, related_name='contact_info')
    location = models.TextField()
    phone_number = models.TextField()

    class Meta:
        ordering = ['-id',]
        verbose_name = "Branch Office"
        verbose_name_plural = "Branch Office"






class OurTeam(models.Model):
    full_name = models.CharField(max_length= 150)
    position = models.CharField(max_length=250)
    image = models.ImageField(upload_to='teamimage/')
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    class MetaL:
        ordering = ['id']
        verbose_name = "Our Team"
        verbose_name_plural = "Our Teams"
    
    def __str__(self):
        return self.full_name

class Blog(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blogimage/')
    discriptions = RichTextField()
    created_date = models.DateField(auto_now_add=True)
    blog_slug = AutoSlugField(populate_from ='title', unique=True, default=None)

    class Meta:
        ordering = ['-id']
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
    
    def __str__(self):
        return self.title



class University(models.Model):
    university_name  = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from ='university_name', unique=True, default=None)

    class Meta:
        ordering =['id',]
        verbose_name = "University In Canada"
        verbose_name_plural = "universities In Canada"
    
    def __str__(self):
        return self.university_name

class UniversityDetails(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='university')
    image = models.ImageField(upload_to='unversityimage/')
    discriptions = RichTextField()

    class Meta:
        ordering =['-id',]
        verbose_name ="University Detail"
        verbose_name_plural ="Universities Details"

    
class CustomerQuery(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone_number = PhoneNumberField()
    message  = models.TextField()


    class Meta:
        ordering = ['-id',]
        verbose_name ="Customer Query"
        verbose_name_plural ="Customer Queries"

    def __str__(self):
        return self.firstname

    
class Services(models.Model):
    image = models.ImageField(upload_to='servicesimage/')
    service_title = models.CharField(max_length=150)
    discriptions = RichTextField()
    service_slug = AutoSlugField(populate_from='service_title', unique=True, default=None)

    class Meta:
        ordering = ['id',]
        verbose_name ="Service"
        verbose_name_plural ="Services"

    def __str__(self):
        return self.service_title
    


class Settings(models.Model):
    meta_keywords = models.TextField()
    meta_discriptions = models.TextField()
    author = models.TextField()

    class Meta:
        ordering = ['-id',]
        verbose_name ="setting"
        verbose_name_plural ="settings"
   
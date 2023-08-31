from django.shortcuts import render, HttpResponse,redirect
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.contrib import messages
from . models import SliderImage,AboutUs,Testimonials,Frequently_Asked_Question,\
    OurTeam,Blog,University,UniversityDetails,CustomerQuery,Services
from django.views.generic import ListView,DetailView
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string,get_template



def index(request):
    slider_images = SliderImage.objects.all()
    firstimage = slider_images[:1]
    about_us = AboutUs.objects.all().order_by('id')[:1]
    testimonials = Testimonials.objects.all()
    faqeven= Frequently_Asked_Question.objects.annotate(odd=F('id') % 2).filter(odd=False)[:3]
    faqodd= Frequently_Asked_Question.objects.annotate(odd=F('id') % 2).filter(odd=True)[:3]
    ourteam = OurTeam.objects.all()[:4]
    services = Services.objects.all()[:6]
    return render(request,'app/index.html',{'slider_images':slider_images[1:],
                                            'firstimage':firstimage,
                                            'about':about_us,
                                            'testimonials':testimonials,
                                            'ourteam':ourteam,
                                            'services':services,
                                            'faqeven':faqeven,
                                            'faqodd':faqodd
                                            })


def about(request):
    about_us = AboutUs.objects.all().order_by('id')
    return render(request,'app/about.html',{'about_us':about_us})


class OurTeamViews(ListView):
    template_name ='app/ourteam.html'
    queryset = OurTeam.objects.all()
    context_object_name = "team_members"

def ourteam(request):
    return render(request,'app/ourteam.html')

def faq(request):
    faq = Frequently_Asked_Question.objects.all()
    faqeven= faq.annotate(odd=F('id') % 2).filter(odd=False)
    faqodd= faq.annotate(odd=F('id') % 2).filter(odd=True)
    return render(request,'app/faq.html',{'faqeven':faqeven,
                                        'faqodd':faqodd})


class BlogListViews(ListView):
    model = Blog
    template_name ='app/blogs.html'
    context_object_name = "blogs"



class BlogDetailView(DetailView):
    model = Blog
    template_name ='app/blogs-pages.html'
    slug_field = 'blog_slug'
    slug_url_kwarg = 'blog_slug'
    # context_object_name = "blogdetails"
    # pk_url_kwarg ='blog_slug'
    # def get_object(self):
    #     allblog = Blog.objects.all()
    #     print(allblog)
    #     obj = get_object_or_404(Blog, blog_slug=self.kwargs['blog_slug'])
    #     return obj

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView,
             self).get_context_data(*args, **kwargs)
        # add extra field
        context["blogdetails"] = get_object_or_404(Blog, blog_slug=self.kwargs['blog_slug']) 
        context['allblog'] = Blog.objects.all()[:7]      
        return context
    
def blog_details(request):
    return render(request,'app/blogs-pages.html')

def contact(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        customerdata = CustomerQuery(firstname=firstname, 
                                     lastname=lastname,
                                    email =email,
                                    phone_number = phone_number,
                                    message=message)
        customerdata.save()
        details ={'fullname':firstname +lastname,
                      'email':email,
                      'phone':phone_number,
                      'message':message
                      }
        subject = "Customer Query Details "
        message = get_template('app/querydetails.html').render(details)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email_from]
        send_mail(subject, message, email_from, recipient_list)

        subject = "Toronto Education Consulting Services"
        message = render_to_string('app/mail.html')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email']]
        send_mail(subject, message, email_from, recipient_list)
    
        messages.success(request,"Query Sbumited Successfully..")
        return redirect(contact)
    else:
        return render(request,'app/contact.html')


class UniversityDetailsViews(DetailView):
    model = University
    template_name ='app/university-pages.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, *args, **kwargs):
        context = super(UniversityDetailsViews,self).get_context_data(*args, **kwargs)
        related_university = get_object_or_404(University, slug=self.kwargs['slug']) 
        print(related_university)
        context["universitydetails"] = UniversityDetails.objects.filter(university = related_university).first()     
        return context
    

class ServiceDetailView(DetailView):
    model = Services
    template_name ='app/servicedetails.html'
    slug_field = 'service_slug'
    slug_url_kwarg = 'service_slug'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ServiceDetailView,self).get_context_data(*args, **kwargs)
        context["servicedetail"] =get_object_or_404(Services, service_slug=self.kwargs['service_slug']) 
        context["services"]= Services.objects.all()
        return context



def CustomerQueries(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        customerdata = CustomerQuery(firstname=firstname, 
                                     lastname=lastname,
                                    email =email,
                                    phone_number = phone_number,
                                    message=message)
        customerdata.save()
        details ={'fullname':firstname +lastname,
                      'email':email,
                      'phone':phone_number,
                      'message':message
                      }
        subject = "Customer Query Details "
        message = get_template('app/querydetails.html').render(details)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email_from]
        send_mail(subject, message, email_from, recipient_list)

        subject = "Toronto Education Consulting Services"
        message = render_to_string('app/mail.html')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email']]
        send_mail(subject, message, email_from, recipient_list)
    
        messages.success(request,"Query Sbumited Successfully..")
        return redirect(index)
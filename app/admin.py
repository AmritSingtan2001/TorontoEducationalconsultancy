from django.contrib import admin
from . models import SliderImage,AboutUs,Testimonials,Frequently_Asked_Question,\
    OurTeam,Blog,University,UniversityDetails,CustomerQuery,Services,Settings,\
    Contact_Info,HeadOffice,BranchOffice


admin.site.site_header = 'Toronto Admin Panel'        
admin.site.index_title = 'Toronto Nepal'                
admin.site.site_title = 'Welcome to Toronto admin panel' 


class SliderImageAdmin(admin.ModelAdmin):
    model:SliderImage
    list_display =['id','image']
admin.site.register(SliderImage,SliderImageAdmin)


class AboutUsAdmin(admin.ModelAdmin):
    model:AboutUs
    list_display =['title','image']
admin.site.register(AboutUs, AboutUsAdmin)

class TestimonialsAdmin(admin.ModelAdmin):
    model: Testimonials
    list_display = ['full_name','image']
admin.site.register(Testimonials,TestimonialsAdmin)


class Frequently_Asked_QuestionAdmin(admin.ModelAdmin):
    model:Frequently_Asked_Question
    list_display =['title','discriptions']
admin.site.register(Frequently_Asked_Question, Frequently_Asked_QuestionAdmin)


class OurTeamAdmin(admin.ModelAdmin):
    model:OurTeam
    list_display =['full_name','position','image']
admin.site.register(OurTeam,OurTeamAdmin)


class BlogAdmin(admin.ModelAdmin):
    model :Blog
    list_display = ['title','image','created_date']
admin.site.register(Blog,BlogAdmin)


class UniversityDetailsAdmin(admin.TabularInline):
    model =  UniversityDetails
    extra = 1

class UniversityAdmin(admin.ModelAdmin):
    inlines =[
        UniversityDetailsAdmin
    ]
    list_display = ['university_name',]
admin.site.register(University, UniversityAdmin)


class CustomerQueryAdmin(admin.ModelAdmin):
    model:CustomerQuery
    list_display =['firstname','lastname','email','phone_number','message']
admin.site.register(CustomerQuery, CustomerQueryAdmin)



class ServicesAdmin(admin.ModelAdmin):
    model:Services
    list_display = ['service_title','image']
admin.site.register(Services,ServicesAdmin)


class SettingsAdmin(admin.ModelAdmin):
    model: Settings
    list_display = ['author','meta_keywords','meta_discriptions']
admin.site.register(Settings,SettingsAdmin)


class HeadOfficeAdmin(admin.TabularInline):
    model =HeadOffice
    extra = 1


class BranchOfficeAdmin(admin.TabularInline):
    model =BranchOffice
    extra = 1

class ContactInfoAdmin(admin.ModelAdmin):
    inlines =[
        HeadOfficeAdmin,BranchOfficeAdmin
    ]
    list_display = ['location','phone_number','email','map_url']
admin.site.register(Contact_Info, ContactInfoAdmin)
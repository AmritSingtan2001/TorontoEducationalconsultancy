from django.urls import path
from . import views
from .views import OurTeamViews,BlogListViews,BlogDetailView,UniversityDetailsViews,ServiceDetailView

urlpatterns = [
    path('', views.index, name ='index'),
    path('about', views.about, name='about'),
    # path('ourteam', OurTeamViews.as_view(), name ='ourteam'),
    # path('ourteam', views.ourteam, name='ourteam'),
    path('faq',views.faq, name='faq'),
    path('blog', BlogListViews.as_view(), name='blog'),
    path('blog/<slug:blog_slug>', BlogDetailView.as_view(), name="blog_details"),
    path('contact', views.contact, name='contact'),
    path('university/<slug:slug>/details', UniversityDetailsViews.as_view(), name='university_details'),
    path('customerqueries', views.CustomerQueries, name='customerqueris'),
    path('services/details/<slug:service_slug>', ServiceDetailView.as_view(), name='service_details'),
]

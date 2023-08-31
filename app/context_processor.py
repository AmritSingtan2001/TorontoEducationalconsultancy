from . models import University,Settings,Contact_Info,HeadOffice,BranchOffice,AboutUs

def university_list(request):
    all_university = University.objects.all()
    return{
        'all_universities':all_university
        }

def about(request):
    about = AboutUs.objects.last()
    return {
        'about':about
    }

def metasettings(request):
    meta_data = Settings.objects.first()
    return{
        'meta_setting':meta_data
    }


def contact_info(request):
    contact_infos = Contact_Info.objects.first()
    return {
        'contact_info':contact_infos
    }

def headoffice(request):
    headoffice_details = HeadOffice.objects.first()
    return{'head_office':headoffice_details}

def branchoffice(request):
    branch_office_details = BranchOffice.objects.first()
    return {
        'branch_office':branch_office_details
    }
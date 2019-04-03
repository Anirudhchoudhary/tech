from django.shortcuts import render
from .forms import Contractor_Form
from .models import Contractor,School
from django.contrib import messages
from django.views.generic import CreateView,UpdateView
from django.views.generic import ListView , DetailView 
from django.http import Http404
# Create your views here.


class Create_Contractor(CreateView):
    model = Contractor
    fields = ['name','Money','area','Time','Image','email','Reason']
    template_name = 'contractor/Create.html'
    success_url = '/'

class List_Contractor(ListView):
    model = Contractor
    template_name = 'contractor/list_contract.html'

    def get_context_data(self ,**kwargs):
        context = super(List_Contractor ,self).get_context_data(**kwargs)
        contract_list = Contractor.objects.get_contract(request = self.request)
        # context['object_list'] = chain(snap_list , item)
        context['contract_list'] = contract_list
        return context     

class Contract_Detail(DetailView):
    queryset = Contractor.objects.all()
    template_name = "contractor/contract_details.html"


class School_List(ListView):
    model = School
    template_name = "school/school_list.html"

    def get_context_data(self ,**kwargs):
        context = super(School_List ,self).get_context_data(**kwargs)
        school_list = School.objects.all()
        top_five_teacher = school_list.order_by('-Teacher')[:5]
        top_five_student = school_list.order_by('-student')[:5]
        top_school_staff = school_list.order_by('-support_staff')[:5]
        top_five_BHAV = school_list.filter(School_level = 'BHAV')
        top_five_HS = school_list.filter(School_level = 'HS')
        top_five_school = school_list.order_by('-Long')[:5]
        context['top_five_school'] = top_five_school
        context['top_five_BHAV'] = top_five_BHAV
        context['top_five_teacher'] = top_five_teacher
        context['top_five_hs'] = top_five_HS
        context['top_five_student'] = top_five_student
        context['top_school_staff'] = top_school_staff

        context['school_list'] = school_list
        return context 


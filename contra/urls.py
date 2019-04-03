from django.urls import path
from .views import Create_Contractor,List_Contractor,Contract_Detail,School_List

app_name = 'contract'

urlpatterns = [
    path('create/',Create_Contractor.as_view(),name = 'create_contract'),
    path('list/',List_Contractor.as_view(),name = 'list_contract'),
    path('Contract/<pk>/',Contract_Detail.as_view() , name = 'contract_details'),
    path('school/list/',School_List.as_view(),name = 'school_list')
]
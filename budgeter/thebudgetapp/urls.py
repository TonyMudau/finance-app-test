from django.urls import path, include
from django.contrib import admin
#now import the views.py file into this code
from . import views

urlpatterns=[
  path('',views.home, name='home'),
  path(r'my-details/',views.MyDetails, name='mydetails'),
  
  
  
  
  path(r'center/',views.Center, name='services'),
  path(r'fis/',views.FIS, name='FIS'),
  path(r'consent',views.consent, name='consent'),
  path(r'login/',views.loginPage, name='login'),
  path(r'logout/',views.logoutUser, name='logout'),
  path(r'my-details/',views.CreateAboutmeDetails, name='my-details'),
  path(r'daily-budget/<str:pk>/',views.DailyBudget, name='daily-budget'),
  path(r'update-details/<str:pk>/',views.EditAboutmeDetails, name='update-details'),
  path(r'dashboard/<str:pk>/',views.DashBoard, name='dashboard'),
  path(r'buyclothservice/',views.BuyClothService, name='buycloth'),
  path(r'logedhome/<str:pk>/',views.LoggedInHome, name='logedhome'),
  #path('',views.Send_prod_data, name='home'),
   
  #===================HTMX URLS =======================================================
  path('my-details/pop_working_option/',views.popworkingoption, name='pop_working_option'),
  path('my-details/pop_ownabusiness_option/',views.popownabusinessoption, name='pop_ownabusiness_option'),
  path('my-details/pop_ownshares_option/',views.popsharesoption, name='pop_ownshares_option'),
  path('my-details/pop_sideincome_option/',views.popsideincomeoption, name='pop_sideincome_option'),
  path('my-details/pop_RentOrBond_option/',views.pop_RentOrBond_option, name='pop_RentOrBond_option'),
  path('my-details/pop_electricity_option/',views.popelectricityoption, name='pop_electricity_option'),
  path('my-details/pop_address_option/',views.popaddressoption, name='pop_address_option'),
  path('my-details/pop_petowner_option/',views.poppetowneroption, name='pop_petowner_option'),
  path('my-details/pop_schoolfees_option/',views.popschoolfeesoption, name='pop_schoolfees_option'),
  path('my-details/pop_ownacar_option/',views.popownacaroption, name='pop_ownacar_option'),
  path('my-details/pop_cellphonecontract_option/',views.popcellphonecontractoption, name='pop_ownacar_option'),
  path('my-details/pop_healthinsurance_option/',views.pophealthinsuranceoption, name='pop_healthinsurance_option'),
  path('my-details/pop_lifeinsurance_option/',views.poplifeinsuranceoption, name='pop_lifeinsurance_option'),
  path('my-details/pop_studentloan_option/',views.popstudentloanoption, name='pop_studentloan_option'),
  path('my-details/pop_otherloans_option/',views.popotherloansoption, name='pop_otherloans_option'),
  path('my-details/pop_retirement_option/',views.popretirementoption, name='pop_retirement_option'),
  path('consent/ConsentPhrases/',views.ConsentPhrases, name='ConsentPhrases'),
  path('mainbase/HomePhrases/',views.HomePhrases, name='HomePhrases'),
  ]
  
  
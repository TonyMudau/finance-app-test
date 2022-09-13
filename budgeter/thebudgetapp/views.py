from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import *
from .forms import *
import random


#==================GLOBAL FUNCTIONS ===============================================

def SayHiToUser(request,title):
    if request.user.is_authenticated:
        return f'Hi, {request.user}'
    else:
        return f'{title}' 

#====================HOME PAGE =====================================================
#Before login
def home(request):
    if request.user.is_authenticated:
        return redirect('logedhome', pk=request.user.id) 
    usname = SayHiToUser(request, 'FinApps')
    context = {'usname':usname}
    return render(request, 'userformapp/main-center.html',context)
    
#After login
@login_required(login_url='/')
def LoggedInHome(request, pk):
    usname = SayHiToUser(request, 'FinApps')
    expenses_form = Expenses.objects.get(user_id=pk)
    data = expenses_form.__dict__
    
    ExpenseMap = []
        
    for key, value in data.items():
        if str(type(value)) == "<class 'decimal.Decimal'>" and value>0:
            print('working')
            ExpenseMap.append({'x': key,'y': float(value)})

    #ExpenseMap = [{'x': 'Rent','y': 100 }, {'x': 'Car Payment','y': 149}, {'x': 'Electricity','y': 184}]

    context = {'usname':usname,'ExpenseMap':ExpenseMap}
    return render(request, 'userformapp/loggedin-center.html',context) 
    
#===================APPS==========================================================


def MyDetails(request): 
    usname = SayHiToUser(request, 'Use our services free')
    context = {'usname':usname}
    return render(request, 'userdetails/my-details.html',context)   

@login_required(login_url='consent')
def DailyBudget(request, pk):
    usname = SayHiToUser(request, 'Use our services free')
    context = {'usname':usname}
    return render(request, 'calenderapp/dailybudget.html',context) 
    
    
@login_required(login_url='consent')
def DashBoard(request, pk):
    usname = SayHiToUser(request, 'Use our services free')
    context = {'usname':usname}
    return render(request, 'dashboard/dashboard.html',context)

@login_required(login_url='consent')       
def FIS(request):
    usname = SayHiToUser(request, 'Use our services free')
    context = {'usname':usname}

    return render(request, 'servicesapp/fis.html',context)
    
#===================SIGNUP LOGIN & OUT====================================================
 
#signup page
@csrf_protect
def signupPage(request):
    if request.user.is_authenticated:
        return redirect('center')
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user )                
                return redirect('login')
            
        context = {'form': form}
        return render(request, 'budapp/signup.html', context)


#login page 
@csrf_protect
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('logedhome')
    else:
          if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
              
            user = authenticate(request, username=username, password=password)
              
            if user is not None:
              #if user logins for 1st time
              #redirect to aboutme
              if user.last_login is None:
                  login(request, user)
                  return redirect('consent')
              else:
                  login(request, user)
                  return redirect('logedhome',pk=user.pk)      
            else:
              messages.info(request, 'Email or Password is incorrect')
          context = {'usname': SayHiToUser(request, 'Login')}   
          return render(request, 'userdetails/login.html', context)

#Logout
def logoutUser(request):
	logout(request)
	return redirect('home')
 
#===============================APP PAGES====================================
#consent
def consent(request):
    return render(request, 'userdetails/consent.html',{'usname': SayHiToUser(request, 'Adding details'),})



def Center(request):
    usname = SayHiToUser(request, 'Use our services free')
    context = {'usname':usname}
    return render(request, 'userformapp/main-center.html')
    


#==========================USER FINANCIALS FORM======================================
#signup page (1st time user)
@csrf_protect
def CreateAboutmeDetails(request):
    userform = CreateUserForm()
    UserFinancials_Form_1 = UserFinancialsForm_1()
    UserFinancials_Form_2 = UserFinancialsForm_2()
    UserFinancials_Form_3 = UserFinancialsForm_3()
    Address_Form = AddressForm()
    Property_Form = PropertyForm()
    Expenses_Form = ExpensesForm()
    Contracts_Form = ContractsForm()

    
    if request.method == 'POST':
        Userform = CreateUserForm(request.POST)
        username = request.POST['username']
        password = request.POST['password1']
        UserFinancials_Form_1 = UserFinancialsForm_1(request.POST)
        UserFinancials_Form_2 = UserFinancialsForm_2(request.POST)
        UserFinancials_Form_3 = UserFinancialsForm_3(request.POST)
        Address_Form = AddressForm(request.POST)
        Property_Form = PropertyForm(request.POST)
        Expenses_Form = ExpensesForm(request.POST)
        Contracts_Form = ContractsForm(request.POST)
        
        if Userform.is_valid():
            user = Userform.save()
            print('saved')
            user = authenticate(request, username=username, password=password)
            #we log the user in before processing other details
            login(request, user)

            if user is not None:
                forms_to_save = [UserFinancials_Form_1, UserFinancials_Form_2, \
                UserFinancials_Form_3, Address_Form, Property_Form, Expenses_Form, Contracts_Form]
                
                if [i.is_valid() for i in forms_to_save]:
                    def save_to_db(form_to_save: list):
                        for form in form_to_save:

                            formsaving = form.save(commit=False)
                            formsaving.user = request.user
                            print(request.user)
                            formsaving.save()
                            
                    save_to_db(forms_to_save)
                    messages.success(request, 'Account was created for ' + username ) 
                    return redirect('logedhome',pk=user.pk)
        else:
            messages.info(request, 'Ensure Passwords match, Your password can’t be too similar to your other personal information. Your password must contain at least 8 characters. Your password can’t be a commonly used password. Your password can’t be entirely numeric. ')
    
    context = { 'Notify': 'Please add details for the service to work',
            'usname': SayHiToUser(request, 'Adding details'),
            'userform':userform,
            'UserFinancials_Form_1':UserFinancials_Form_1,
            'UserFinancials_Form_2':UserFinancials_Form_2,
            'UserFinancials_Form_3':UserFinancials_Form_3,
            'Address_Form':Address_Form,
            'Property_Form':Property_Form,
            'Expenses_Form':Expenses_Form,
            'Contracts_Form':Contracts_Form
            }
    return render(request, 'userdetails/my-details.html', context)
#userform after login for the 1st time
#Users must be given the option to edit these details 

#Update form
@csrf_protect
def EditAboutmeDetails(request, pk):
    userfin_form_1 = UserFinancials_page1.objects.get(user_id=pk)#as named in model
    UserFinancialsForm_11 = UserFinancialsForm_1(instance=userfin_form_1)#as named in form
    
    userfin_form_2 = UserFinancials_page2.objects.get(user_id=pk)
    UserFinancialsForm_21 = UserFinancialsForm_2(instance=userfin_form_2)
    
    userfin_form_3 = UserFinancials_page3.objects.get(user_id=pk)
    UserFinancialsForm_31 = UserFinancialsForm_3(instance=userfin_form_3)  
    
    address_details = Address_details.objects.get(user_id=pk)
    Address_Form1 = AddressForm(instance=address_details) 
    
    property_form = Property.objects.get(user_id=pk)
    Property_Form1 = PropertyForm(instance=property_form)  
    
    expenses_form = Expenses.objects.get(user_id=pk)
    Expenses_Form1 = ExpensesForm(instance=expenses_form)  
    
    contracts_form = Contracts.objects.get(user_id=pk)
    Contracts_Form1 = ContractsForm(instance=contracts_form)  
    
    if request.method == 'POST':
        UserFinancials_Form_1 = UserFinancialsForm_1(request.POST, instance=userfin_form_1)
        UserFinancials_Form_2 = UserFinancialsForm_2(request.POST, instance=userfin_form_2)
        UserFinancials_Form_3 = UserFinancialsForm_3(request.POST, instance=userfin_form_3)
        Address_Form = AddressForm(request.POST, instance=address_details)
        Property_Form = PropertyForm(request.POST, instance=property_form)
        Expenses_Form = ExpensesForm(request.POST, instance=expenses_form)
        Contracts_Form = ContractsForm(request.POST, instance=contracts_form)

        forms_to_save = [UserFinancials_Form_1, UserFinancials_Form_2, UserFinancials_Form_3, Address_Form, Property_Form,\
                                  Expenses_Form, Contracts_Form]
             
        if [i.is_valid() for i in forms_to_save]:
            def save_to_db(form_to_save: list):
                for form in form_to_save:
                    form.save()
                    
            save_to_db(forms_to_save)
            messages.success(request, 'Financial details have been Updated') 
            return redirect('home')
            
    context = { 'Notify': 'Please add details for the service to work',
            'usname': SayHiToUser(request, 'Updating details'),
            'UserFinancials_Form_1':UserFinancialsForm_11,
            'UserFinancials_Form_2':UserFinancialsForm_21,
            'UserFinancials_Form_3':UserFinancialsForm_31,
            'Address_Form':Address_Form1,
            'Property_Form':Property_Form1,
            'Expenses_Form':Expenses_Form1,
            'Contracts_Form':Contracts_Form1
            }
    return render(request, 'userdetails/update-details.html', context)
#userform after login for the 1st time
#Users must be given the option to edit these details 


#==============================SERVICES ===========================================
#A user clicks on of the services from the center page

def BuyClothService(request):
    usname = SayHiToUser(request, 'Use our services free')
    UserFinancials_Form_1 = UserFinancialsForm_1()
    if request.method == 'POST':
        if request.user.is_authenticated == True:
            
                print("=====Forms Saved========")

        else:
            return redirect('consent')

    context = {'usname':usname,'UserFinancials_Form_1':UserFinancials_Form_1}

    return render(request, 'servicesapp/buyclothservice.html',context)
    
  

#==================HTMX FUNCTIONS ================================================

#This function is the main function that will take in 
#trigger attributes for a drop down to return a new field
def triggerform(request,formname,trigger,fieldnametarget,label):
    Form_1 = formname
    Trigger = request.GET.get(trigger)
    if Trigger == 'Y' or Trigger == 'R':
        FormField = Form_1[fieldnametarget]
        return HttpResponse(f'<label for="fieldnametarget">{label}</label><br> { FormField }')
    else:
        return HttpResponse(' ')
        
               
#This function will display the income input 
#when a user clicks Yes for Are you working?
def popworkingoption(request):
    return triggerform(request, UserFinancialsForm_1(),'Working','Income','Income after tax?')   

def popownabusinessoption(request):
    return triggerform(request, UserFinancialsForm_2(),'OwnABusiness','BusinessIncome', 'Average Monthly salary you recieve from your business?')     

def popsharesoption(request):
    return triggerform(request, UserFinancialsForm_2(),'OwnShares','SharesWorth', 'Total shares current value?')
 
def popsideincomeoption(request):
    return triggerform(request, UserFinancialsForm_3(),'SideIncome','MonthlySideIncome','What is your average montly side income?')

#if user pays bond .. return extra fields regarding bond
def pop_RentOrBond_option(request):
    Form_1 = PropertyForm()
    Trigger = request.GET.get('RentOrBond')
    if Trigger == 'B':
        RentingBondingPayment = Form_1['RentingBondingPayment']
        YearsLeftOfBond = Form_1['YearsLeftOfBond']
        InterestOnBond = Form_1['InterestOnBond']
        Rates = Form_1['Rates']
        #form for bond
        bond_form_to_render = f"""
        <label for="RentingBondingPayment">Monthly Bond Payment</label><br> { RentingBondingPayment } <br>
        <label for="YearsLeftOfBond">How many years do you have left in paying your bond?</label><br> { YearsLeftOfBond } <br> 
        <label for="InterestOnBond">Whats the interest on your bond?</label><br> { InterestOnBond }  <br>
        <label for="Rates">Average monthly rates and taxes on property?</label><br> { Rates }  <br>    

        """  
        return HttpResponse(f'{bond_form_to_render}')
    else:
        return triggerform(request, PropertyForm(),'RentOrBond','RentingBondingPayment','How much do you pay in rent?')

def popelectricityoption(request):
    return triggerform(request, ExpensesForm(),'Electricity','ElectricityPayment','Monthly expenditure on electricity?')

#Address form
def popaddressoption(request):
    Form_1 = AddressForm()
    Trigger = request.GET.get('AddressOption')
    if Trigger == 'Y':
        StreetName = Form_1['StreetName']
        City = Form_1['City']
        Province = Form_1['Province']
        Country = Form_1['Country']
   
        address_form_to_render = f"""
        <label>StreetName</label><br> { StreetName } <br>
        <label>City</label><br> { City } <br> 
        <label>Province</label><br> { Province }  <br>
        <label>Country</label><br> { Country }  <br>    

        """  
        return HttpResponse(f'{address_form_to_render}') 
    else:
        return HttpResponse(' ')
    
       
def poppetowneroption(request):
    return triggerform(request, ExpensesForm(),'PetOwner','PetsPayment','Monthly expenditure on your pets including insurance?')  
    
    
def popschoolfeesoption(request):
    return triggerform(request, ContractsForm(),'SchoolFees','SchoolFeesPayment','Total Monthly school fees payment?')   
    
def popownacaroption(request):
    return triggerform(request, ContractsForm(),'OwnACar','CarPayment','Monthly car installment, including insurance?')
    
def popcellphonecontractoption(request):
    return triggerform(request, ExpensesForm(),'CellPhoneContract','CellphonePayment','Monthly cellphone contract payment?')
    
def pophealthinsuranceoption(request):
    return triggerform(request, ContractsForm(),'HealthInsurance','HealthInsurancePayment','Monthly health insurance payment?')
    
def poplifeinsuranceoption(request):
    return triggerform(request, ContractsForm(),'LifeInsurance','LifeInsurancePayment','Monthly life insurance payment?') 
    
    
def popstudentloanoption(request):
    Form_1 = ContractsForm()
    Trigger = request.GET.get('StudentLoan')
    if Trigger == 'Y':
        StudentLoanPayment = Form_1['StudentLoanPayment']
        YearsLeftOfStudentLoan = Form_1['YearsLeftOfStudentLoan']
        InterestOnStudentLoan = Form_1['InterestOnStudentLoan']
        #form for bond
        studentloan_form_to_render = f"""
        <label for="StudentLoanPayment">Student Loan amount remaining?</label><br> { StudentLoanPayment } <br>
        <label for="YearsLeftOfStudentLoan">How many years do you have left in paying your student loan?</label><br> { YearsLeftOfStudentLoan } <br> 
        <label for="InterestOnStudentLoan">Whats the interest on your student loan?</label><br> { InterestOnStudentLoan }  <br>
       

        """  
        return HttpResponse(f'{studentloan_form_to_render}')
    else:
        return HttpResponse(' ')  
    
def popotherloansoption(request):
    Form_1 = ContractsForm()
    Trigger = request.GET.get('OtherLoans')
    if Trigger == 'Y':
        OtherLoansPayment = Form_1['OtherLoansPayment']
        YearsLeftOfOtherLoans = Form_1['YearsLeftOfOtherLoans']
        InterestOnOtherLoans = Form_1['InterestOnOtherLoans']
        #form for bond
        otherloan_form_to_render = f""" 
        <label for="OtherLoansPayment">Other Loan amount remaining?</label><br> { OtherLoansPayment } <br>
        <label for="YearsLeftOfOtherLoans">How many years do you have left in paying your other loan?</label><br> { YearsLeftOfOtherLoans } <br> 
        <label for="InterestOnOtherLoans">Whats the interest on your other loan?</label><br> { InterestOnOtherLoans }  <br>
       

        """  
        return HttpResponse(f'{otherloan_form_to_render}')
    else:
        return HttpResponse(' ')    
    
def popretirementoption(request):
    return triggerform(request, ContractsForm(),'Retirement','RetirementPayment','Monthly retirement contribution?')    
    
    
def ConsentPhrases(request):
    word = ["We don't sell data","We don't identify you", "We just help","All data is cloud secure"]
    phrase = random.choice(word)
    return HttpResponse(f'{ phrase }')
    
def HomePhrases(request):
    word = ["Saving in this economy?","Get easy financial information", "How can technology help you?", "Try our services","Looking for custom financial information?"]
    phrase = random.choice(word)
    return HttpResponse(f'{ phrase }')
    
#=============================APEX CHARTS DASHBOARDS =======================================================




#==================================================Get products =============================================



from anyio import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd 
from datetime import datetime, date
import json, time
from requests_html import HTMLSession
import asyncio






def Send_prod_data(request):
    our_product_data = {} 
    test = []
    if request.method == 'POST':
        search_word = request.POST.get('task')
        print(search_word)
        url = f'https://www.guzzle.co.za/specials/search/?q={search_word}'
        s = HTMLSession()
        r = s.get(url)
        
        
        
       
        #r.html.render(sleep=0.5,scrolldown=7,timeout = 30)
        prod_table = r.html.find('.deals-range', first=True)
        
 
        sou = prod_table.html
        print(sou)
        soup = BeautifulSoup(sou, "lxml")
        
        
        
        
        def get_product_links():
            links = []
            for i in prod_table.links:
                #if not 'guzzle' in i:
                links.append(i[:-92])
            
            return links
        
        
        def get_product_images():
            images = []
            for link in soup.findAll('img'):
                img = link.get('src')
                if img[-3:] == 'jpg':
                    images.append(img)
            return images
        
        
        def get_product_names():
            names = []
            lst = prod_table.text.splitlines()[::5]
            for i in lst:
                if not i[0] == 'R':
                    names.append(i)
            return names
        
        
        # print(prod_table[0].text)
        
        def get_product_prices():
            prices = []
            lst = prod_table.text.splitlines()
            for i in lst:
                if i[0] == 'R' and len(i) < 9:
                    prices.append(i)
            return prices 
        
        res = dict(zip(get_product_names(), get_product_prices()))
        
        #print(len(res))
        
        a = get_product_names()[:20]
        
        b = get_product_images()[:20]
        c = get_product_links()[:20]
        d = get_product_prices()[:20]
        
        e = get_product_names()[:20]
        
        f = get_product_names()[:20]
        
        
        print(a, d)
        
        test = zip(a, b, c, d, e, f)
        
        
        
        vals = zip(b,c,d)
        our_product_data = dict(zip(a,vals))
        print(our_product_data)
        
        s.close()
      

    context = {'our_product_data':our_product_data,
                'test':test}
    return render(request, 'userformapp/search.html', context)






















from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

select_attrs = {'class': 'btn btn-outline-dark dropdown-toggle',
                                                    'style':'background-color: #16b8f8 !important',
                                                    'text-align': 'center'}

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'  
        
class ClientNameForm(ModelForm):
    class Meta:
        model = ClientName
        fields = ['name'] 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
            }
            
        
class UserFinancialsForm_1(ModelForm):
    class Meta:
        model = UserFinancials_page1
        fields = ['age','lifeRole','NoOfDependants','Working','Income']   
        widgets = {
            'age': forms.Select(attrs=select_attrs),
            'lifeRole': forms.Select(attrs=select_attrs),
                                                    
            'NoOfDependants': forms.Select( attrs=select_attrs),
                                                    
            'Working': forms.Select( attrs=select_attrs),
            'Income': forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
        
        }
        
        
        
        
class UserFinancialsForm_2(ModelForm):
    class Meta:
        model = UserFinancials_page2
        fields = ['OwnABusiness','BusinessIncome','OwnShares','SharesWorth']   
        widgets = {
            
            
            'OwnABusiness': forms.Select( attrs=select_attrs),
                                                    
            'BusinessIncome':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
            
            'OwnShares': forms.Select( attrs=select_attrs),  
            'SharesWorth': forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),      
        }
        
        
class UserFinancialsForm_3(forms.ModelForm):
    class Meta:
        model = UserFinancials_page3
        fields = ['SideIncome','MonthlySideIncome']   
        widgets = {
            'SideIncome': forms.Select( attrs=select_attrs),
            'MonthlySideIncome':forms.NumberInput( attrs={'class': 'form-control','placeholder':'R'}),       
        }
        
        

class AddressForm(ModelForm):
    class Meta:
        model = Address_details
        fields = ['AddressOption','StreetName','City','Province','Country']
        widgets = {
            'AddressOption' : forms.Select( attrs=select_attrs),
            'StreetName': forms.TextInput(attrs={'class': 'form-control'}),
            'City': forms.TextInput(attrs={'class': 'form-control'}),
            'Province':forms.TextInput(attrs={'class': 'form-control'}),   
            'Country':forms.TextInput(attrs={'class': 'form-control'})    
        }    
        
        
class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = ['RentOrBond','YearsLeftOfBond','InterestOnBond','RentingBondingPayment','Rates']
        widgets = {
                  'RentOrBond':forms.Select( attrs=select_attrs),
                  'YearsLeftOfBond':forms.NumberInput(attrs={'class': 'form-control'}),
                  'InterestOnBond':forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'%'}),
                  'RentingBondingPayment':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
                  'Rates':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),      
                  }


          
               
class ExpensesForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['Groceries','Transport','Entertainment','Savings','Electricity','ElectricityPayment','MembershipsAndSubscriptions','PetOwner','PetsPayment','InternetAndData','CellPhoneContract','CellphonePayment']   
        widgets = {        
                  'Groceries':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
                  'Transport':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
                  'Entertainment':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
                  'Savings':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
                  'Electricity':forms.Select( attrs=select_attrs),
                  'ElectricityPayment':forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'R'}),  
                  'MembershipsAndSubscriptions':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
                  'PetOwner':forms.Select( attrs=select_attrs),
                  'PetsPayment':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
                  'InternetAndData':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
                  'CellPhoneContract': forms.Select( attrs=select_attrs),
                  'CellphonePayment':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
        }      



 
class ContractsForm(ModelForm):
    class Meta:
        model = Contracts
        fields = ['NoOfContracts','SchoolFees','SchoolFeesPayment','OwnACar','CarPayment',\
        'HealthInsurance','HealthInsurancePayment','LifeInsurance','LifeInsurancePayment',\
        'StudentLoan','StudentLoanPayment','YearsLeftOfStudentLoan','InterestOnStudentLoan','OtherLoans','OtherLoansPayment',\
        'YearsLeftOfOtherLoans','InterestOnOtherLoans','Retirement','RetirementPayment']
        widgets = {
              'NoOfContracts':forms.Select(attrs=select_attrs),                 
      		    'SchoolFees': forms.Select( attrs=select_attrs),
              'SchoolFeesPayment':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
              'OwnACar': forms.Select( attrs=select_attrs),
              'CarPayment':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
              #'CarInsurance': forms.Select( attrs=select_attrs),
              #'CarInsurancePayment':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
              
              'HealthInsurance': forms.Select( attrs=select_attrs),
              'HealthInsurancePayment':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
              'LifeInsurance': forms.Select( attrs=select_attrs),
              'LifeInsurancePayment':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
              'StudentLoan': forms.Select( attrs=select_attrs),
              'StudentLoanPayment':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
              'YearsLeftOfStudentLoan': forms.NumberInput(attrs={'class': 'form-control'}),
              'InterestOnStudentLoan': forms.NumberInput(attrs={'class': 'form-control','placeholder':'%'}),
              'OtherLoans': forms.Select( attrs=select_attrs),
              'OtherLoansPayment':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
              'YearsLeftOfOtherLoans': forms.NumberInput(attrs={'class': 'form-control'}),
              'InterestOnOtherLoans': forms.NumberInput(attrs={'class': 'form-control','placeholder':'%'}),
              'Retirement': forms.Select( attrs=select_attrs),
              'RetirementPayment':forms.NumberInput(attrs={'class': 'form-control','placeholder':'R'}),
              
              
        }          
              
        

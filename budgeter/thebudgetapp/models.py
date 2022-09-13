from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
#from django_userforeignkey.models.fields import UserForeignKey
# Create your models here.


# Need to have a max (4) number of fields 
#per section. 


#Tony
CHOICES =[
    ('0','0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6+')
    ]

YES_NO = [
    ('Y', 'Yes'),
    ('N', 'No')
]

LIFE_ROLES = [
    ('mother','Mother'),
    ('father','Father'),
    ('Gran','GrandParent'),
    ('student','Student'),
    ('child','Son or Daughter'),
    ('Bachelor','Bachelor')
]

RENT_BOND = [('N','None'),
             ('B','Bond'),
             ('R','Rent'),            
]

AGE = [
      ('18','<18'),
      ('1924','19-24'),
      ('2530','25-30'),
      ('3135','31-35'),
      ('3640','36-40'),
      ('4145','41-45'),
      ('4650','46-50'),
      ('5155','51-55'),
      ('5660','56-60'),
      ('60','+60')
      ]

class ClientName(models.Model):
    name = models.CharField('What is your preffered name?', null=False, blank=False, max_length=100)

class UserFinancials_page1(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    age = models.CharField('Age?', null=False, max_length=100, choices=AGE)
    lifeRole = models.CharField('What is your life role of priority?', null=False, max_length=100, choices=LIFE_ROLES)
    NoOfDependants = models.CharField('How many people are dependant to your income?', null=False, max_length=100, choices=CHOICES)
    Working = models.CharField('Are you working for an income?', null=False, max_length=100, choices=YES_NO)
    Income = models.DecimalField('Income after tax',max_digits=12, decimal_places=2,blank=True, null=False, default=0)

    
class UserFinancials_page2(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    OwnABusiness = models.CharField('Are you an owner of a business with cashflow?', null=False, max_length=100, choices=YES_NO)
    BusinessIncome = models.CharField('Average Monthly salary you recieve from your business?',max_length=100,blank=True, null=False, default=0)
    OwnShares = models.CharField('Do you own shares in any company?', null=False, max_length=100, choices=YES_NO)
    SharesWorth = models.CharField('Total shares worth?',max_length=100,blank=True, null=False, default=0)
    
class UserFinancials_page3(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    SideIncome = models.CharField('Do you have a side income?', null=True, max_length=100, choices=YES_NO)
    MonthlySideIncome = models.CharField('Total Monthly side income',max_length=100,blank=True, null=False, default=0)
    
    
class Address_details(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    AddressOption = models.CharField('Would you like to input your address information?', null=False, max_length=100, choices=YES_NO)
    StreetName = models.CharField('Street',max_length=100,blank=True)
    City = models.CharField(max_length=100,blank=True)
    Province = models.CharField("Province",max_length=100,blank=True)
    Country = models.CharField(max_length=100,blank=True)
    
class Property(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    RentOrBond = models.CharField('Are you renting or paying a bond?', null=False, max_length=100, choices=RENT_BOND)
    #if bond, how many years do you have to pay back and Interest rate?
    RentingBondingPayment = models.DecimalField('How much do you pay in rent/bond?',max_digits=12, decimal_places=2,blank=True, null=False, default=0)
    YearsLeftOfBond = models.CharField('How many years do you have left in paying your bond?',max_length=100, null=False, default=0, blank=True)
    InterestOnBond = models.CharField('Whats the interest on your bond?',max_length=100, null=False, default=0, blank=True) 
    Rates = models.DecimalField('Montly rates and levies',max_digits=12, decimal_places=2, null=False, default=0, blank=True)   

    
class Expenses(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    Groceries = models.DecimalField('Monthly expenditure on groceries',max_digits=12, decimal_places=2, null=False)  
    Transport = models.DecimalField('Monthly expenditure on Transport',max_digits=12, decimal_places=2, null=False)
    Electricity = models.CharField('Do you buy electricity where you reside?', null=False, max_length=100, choices=YES_NO)
    ElectricityPayment = models.DecimalField('Monthly expenditure on electricity',max_digits=12, decimal_places=2, null=False, default=0, blank=True)
    MembershipsAndSubscriptions = models.DecimalField('',max_digits=12, decimal_places=2, null=False, default=0, blank=True)
    Entertainment = models.DecimalField('Monthly expenditure on entertainment',max_digits=12, decimal_places=2, null=False)
    Savings = models.DecimalField('Monthly payment to emergency funds',max_digits=12, decimal_places=2,null=False) #should calculate estimate based on income
    PetOwner = models.CharField('Are you a pet owner?', null=False, max_length=100, choices=YES_NO)
    PetsPayment = models.DecimalField('Monthly expenditure on your pets including insurance?',max_digits=12, decimal_places=2, null=False, default=0, blank=True)
    InternetAndData = models.DecimalField('Monthly expenditure on data and airtime?',max_digits=12, decimal_places=2, null=False)
    CellPhoneContract = models.CharField('Do you have a cellphone contract?', null=False, max_length=100, choices=YES_NO)
    CellphonePayment =models.DecimalField('Cellphone contract payment?',max_digits=12, decimal_places=2, null=False, default=0, blank=True)
     
class Contracts(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    NoOfContracts = models.CharField('Number of contracts you pay monthly', null=False, max_length=100, choices=CHOICES)
    SchoolFees = models.CharField('Do you pay school fees?', null=False, max_length=100, choices=YES_NO)
    SchoolFeesPayment = models.DecimalField('School Fees payment',max_digits=12, decimal_places=2,blank=True, null=False, default=0)
    OwnACar = models.CharField('Do you own a car?', null=False, max_length=100, choices=YES_NO)
    CarPayment = models.DecimalField('Car installment',max_digits=12, decimal_places=2,blank=True, null=False, default=0)
    #CarInsurance = models.CharField('Do you pay car insurance?', null=False, max_length=100, choices=YES_NO)
    #CarInsurancePayment = models.DecimalField('Monthly expenditure on car insurance?',max_digits=12, decimal_places=2)
    HealthInsurance = models.CharField('Do you have a cellphone contract?', null=False, max_length=100, choices=YES_NO)
    HealthInsurancePayment = models.DecimalField('',max_digits=12, decimal_places=2, null=False, default=0, blank=True)
    LifeInsurance = models.CharField('Do you have a life insurance policy?', null=False, max_length=100, choices=YES_NO)
    LifeInsurancePayment = models.DecimalField('life insurance policy contract payment?',max_digits=12, decimal_places=2, blank=True, null=False, default=0)
    StudentLoan = models.CharField('Do you have a life insurance policy?', null=False, max_length=100, choices=YES_NO)
    StudentLoanPayment = models.DecimalField('',max_digits=12, decimal_places=2, null=False, default=0, blank=True)
    YearsLeftOfStudentLoan = models.CharField('Years left on student loan?',max_length=100, blank=True, null=False, default=0)
    InterestOnStudentLoan = models.CharField('Interest on student loan?',max_length=100, blank=True, null=False, default=0)
    OtherLoans = models.CharField('Do you have a life insurance policy?', null=False, max_length=100, choices=YES_NO)
    OtherLoansPayment = models.DecimalField('',max_digits=12, decimal_places=2, blank=True, null=False, default=0)
    YearsLeftOfOtherLoans = models.CharField('Years left on other loan?',max_length=100, blank=True, null=False, default=0)
    InterestOnOtherLoans = models.CharField('Interest on other loan?',max_length=100, blank=True, null=False, default=0)
    Retirement = models.CharField('Do you have a life insurance policy?', null=False, max_length=100, choices=YES_NO)
    RetirementPayment = models.DecimalField('',max_digits=12, decimal_places=2, null=False, default=0, blank=True )
    

    

    
    
    
    
    
    
    

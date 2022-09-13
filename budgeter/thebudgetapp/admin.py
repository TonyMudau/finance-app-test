from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ClientName)
admin.site.register(UserFinancials_page1)
admin.site.register(UserFinancials_page2)
admin.site.register(UserFinancials_page3) 
admin.site.register(Expenses)
admin.site.register(Address_details)
admin.site.register(Property)
admin.site.register(Contracts)

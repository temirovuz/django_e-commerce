from django.contrib import admin

from account.models import User, Company, Address, Seller

admin.site.register([User, Company, Address, Seller])

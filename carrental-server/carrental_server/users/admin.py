from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django.db import models

# Register your models here.

# Configuration for admin page
class UserAdminConfig(UserAdmin):
    """
    Configuration for the admin page.
    search_fields defines the list of field names that will be searched when a query is submitted.
    list_filter activates list of field names that can be used as filter on the right sidebar of admin page.
    fieldsets controls the layout of the 'change' and 'add' pages
    add_fieldsets sets the fields in the form to create a new user
    """
    model = NewUser
    search_fields = ('first_name', 'last_name', 'email', 'license_number', 'phone_number')

    list_filter = ('first_name', 'email', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('id', 'first_name', 'last_name', 'email', 'address',
                    'license_number', 'date_of_birth', 'phone_number', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('first_name', 'email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    # formfield_overrides = {
    #     models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 10})},
    # }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'middle_name', 'last_name', 'email', 'address',
                       'license_number', 'date_of_birth', 'phone_number', 'is_active', 'is_staff')}
         ),
    )

admin.site.register(NewUser, UserAdminConfig)

# Third Party Stuff
from django.contrib import admin

from .models import Constituency


class ConstituencyAdmin(admin.ModelAdmin):

    '''
    Admin View for Constituency Data
    '''
    list_display = ('constituency_name', 'state')
    list_filter = ('constituency_name', 'state')
    search_fields = ['constituency_name', 'state', ]


admin.site.register(Constituency, ConstituencyAdmin)
